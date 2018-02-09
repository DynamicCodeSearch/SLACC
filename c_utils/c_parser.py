from __future__ import print_function, division
import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"
from utils import cache, c_ast_gen
from pycparser import c_parser, c_ast, parse_file, c_generator
from pycparser.plyparser import ParseError
from utils.lib import O
from utils.logger import get_logger
import csv
import logging
import re
import subprocess


LOG_LEVEL = logging.INFO
logger = get_logger(__name__, LOG_LEVEL)
csv.field_size_limit(sys.maxsize)
FAKE_LIBS_PATH = "utils/fake_libc_include"
FAKE_FILE_CONTENT = """#include "_fake_defines.h"
#include "_fake_typedefs.h"
"""


def read(sources_file, destination_file, start=0):
  sources = cache.load(sources_file)
  functions = []
  n_rows = len(sources)
  n_errors = 0
  for i, row in enumerate(sources[start:]):
    name = row['path'].rsplit("/", 1)[-1].split(".")[0].split()[0]
    n_functions, n_error = c_extract(row['id'], name, row['content'], repeat=True)
    functions += n_functions
    n_errors += n_error
    if (i + 1) % 100 == 0:
      logger.info("Read %d/%d of files. Errors: %d" % (start + i + 1, n_rows, n_errors))
  cache.save(destination_file, functions)
  return functions


class Arg(O):
  def __init__(self):
    O.__init__(self)
    self.name = None
    self.type = None
    self.is_ptr = False
    self.is_struct = False
    self.is_arr = False
    self.is_enum = False
    self.is_func = False
    self.is_union = False

  @staticmethod
  def parse(node):
    # print(node)
    if isinstance(node, c_ast.EllipsisParam): return None
    arg = Arg()
    arg.name = node.name
    if isinstance(node, c_ast.ID): return arg
    type_node = node.type
    while isinstance(type_node, c_ast.ArrayDecl):
      arg.is_arr = True
      type_node = type_node.type
    while isinstance(type_node, c_ast.PtrDecl):
      arg.is_ptr = True
      type_node = type_node.type
    while isinstance(type_node, c_ast.ArrayDecl):
      arg.is_arr = True
      type_node = type_node.type
    if isinstance(type_node, c_ast.FuncDecl):
      arg.is_func = True
      arg.type = "FUNCTION"
      return arg
    if isinstance(type_node.type, c_ast.Struct):
      arg.is_struct = True
      arg.type = type_node.type.name
    elif isinstance(type_node.type, c_ast.Union):
      arg.is_union = True
      arg.type = type_node.type.name
    elif isinstance(type_node.type, c_ast.Enum):
      arg.is_enum = True
      arg.type = type_node.type.name
    else:
      arg.type = type_node.type.names[0]
    return arg


class Return(O):
  def __init__(self):
    O.__init__(self)
    self.type = None
    self.is_ptr = False
    self.is_struct = False
    self.is_enum = False
    self.is_union = False

  @staticmethod
  def parse(node):
    # print(node)
    ret = Return()
    while isinstance(node, c_ast.PtrDecl):
      ret.is_ptr = True
      node = node.type
    if isinstance(node.type, c_ast.Struct):
      ret.is_struct = True
      ret.type = node.type.name
    elif isinstance(node.type, c_ast.Union):
      ret.is_union = True
      ret.type = node.type.name
    elif isinstance(node.type, c_ast.Enum):
      ret.is_enum = True
      ret.type = node.type.name
    else:
      ret.type = node.type.names[0]
    return ret


class Function(O):
  def __init__(self, name, body):
    O.__init__(self)
    self.name = name
    self.body = body
    self.args = []
    self.ret = None
    self.source_id = None
    self.source_name = None


class FuncDefStatCollector(c_ast.NodeVisitor):
  generator = c_generator.CGenerator()

  def __init__(self, i_d, name):
    self.id = i_d
    self.name = name
    self.functions = []

  def visit_FuncDef(self, node):
    # if node.decl.name == "main":
    #   return None
    func = Function(node.decl.name, FuncDefStatCollector.generator.visit(node))
    func.source_id = self.id
    func.source_name = self.name
    arg_nodes = node.decl.type.args
    if arg_nodes and len(arg_nodes.params) > 0:
      for arg_node in arg_nodes.params:
        arg = Arg.parse(arg_node)
        if arg is not None:
          func.args.append(arg)
      # try:
      #
      # except Exception as e:
      #   print(arg_nodes.params)
      #   raise e

    func.ret = Return.parse(node.decl.type.type)
    self.functions.append(func)
    return func


def c_extract(i_d, name, source, repeat=True):
  """
  Compile c source code.
  :param i_d: ID of row
  :param name: Name of file
  :param source: "Source code as string"
  :return:
  """
  file_name = cache.create_file_path("temp", name, ext=".c")
  collector = FuncDefStatCollector(i_d, file_name.rsplit("/", 1)[-1])
  with open(file_name, "wb") as write:
    write.write(source)
  errors = 0
  try:
    ast, error = parse_c_file(file_name)
    if error and repeat:
      ast, error = parse_c_file(file_name)
    if ast is not None:
      collector.visit(ast)
    else:
      errors += 1
  except (ParseError, AssertionError) as e:
    errors += 1
    # raise e
  cache.delete(file_name)
  return collector.functions, errors


def handle_not_found_exception(message):
  matches = re.search('fatal error: (.+?): No such file or directory', message)
  if matches:
    header_file = cache.create_file_path(FAKE_LIBS_PATH, matches.group(1))
    logger.info("Creating fake header file %s" % header_file)
    cache.save_text(header_file, FAKE_FILE_CONTENT)


def _read():
  sources_file = "data/cfiles_dump/valids/valid.pkl"
  destination_file = "data/cfiles_dump/valids/functions.pkl"
  read(sources_file, destination_file, start=0)


def _test_exception():
  msg = """
  temp/ucon.c:22:23: fatal error: asm/types.h: No such file or directory
   #include <asm/types.h>
  """
  handle_not_found_exception(msg)


def parse_c_file(file_name):
  cmd = ['python', 'utils/c_ast_gen.py', file_name]
  proc = subprocess.Popen(cmd, stderr=subprocess.PIPE)
  error = "".join(proc.stderr.readlines())
  ast = cache.load(c_ast_gen.AST_SAVE)
  cache.delete(c_ast_gen.AST_SAVE)
  if error:
    handle_not_found_exception(error)
  return ast, error


if __name__ == "__main__":
  # _read()
  # _test_exception()
  # parse_file('temp/fixdep.c', use_cpp=True, cpp_args=[r'-I%s' % FAKE_LIBS_PATH])
  # _test_child_process()
  _metrics()
