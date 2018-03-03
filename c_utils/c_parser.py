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
import itertools


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
  FUZZABLE = {"int", "float", "char"}

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

  def is_valid_arg(self):
    return (not self.is_enum) and (not self.is_func) and (not self.is_ptr) and \
           (not self.is_struct) and (not self.is_union) and (not self.is_arr) and \
           (self.type in Arg.FUZZABLE)



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

  def is_valid_ret(self):
    return (not self.is_enum) and (not self.is_ptr) and (not self.is_struct) and \
           (not self.is_union) and (self.type in Arg.FUZZABLE)


def int_vals(limit=True):
  if limit:
    return [-2147483647, -100, -1, 0, 1, 100, 2147483646]
  else:
    return [-2147483647, -10000, -5000, -2000, -1000, -500, -200, -100, -50, -20, -10, -5, -2, -1, 0,
            1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 2147483646]


def float_vals(limit=True):
  if limit:
    return [-3.3E+38, -100.0, -1.0, 0.0, 1.0, 100.0, 3.3E+38]
  else:
    return [-3.3E+38, -10000.0, -5000.0, -2000.0, -1000.0, -500.0, -200.0, -100.0, -50.0, -20.0, -10.0, -5.0, -2.0, -1.0,
            0.0, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0, 200.0, 500.0, 1000.0, 2000.0, 5000.0, 10000.0, 3.3E+38]


def char_vals(limit=True):
  if limit:
    return ["'a'", "'z'", "'~'", "'#'", "'\t'", "'\n'"]
  else:
    return ["'a'", "'c'", "'g'", "'h'", "'f'", "'i'", "'k'", "'o'", "'w'", "'z'",
            "'~'", "'#'", "'\t'", "'\n'", "'0'", "'4'", "'5'", "'9'", "'('", "'|'",
            "'\"'", "'\''"]


class Function(O):
  PRINT_F = re.compile(r'printf\(')
  SCAN_F = re.compile(r'scanf\(')

  def __init__(self, name, body):
    O.__init__(self)
    self.name = name
    self.body = body
    self.args = []
    self.ret = None
    self.source_id = None
    self.source_name = None
    self.source = None
    self.is_static = False

  def check_func_io(self):
    return Function.PRINT_F.search(self.body) is not None, Function.SCAN_F.search(self.body)

  def is_fuzzable(self, arg_limit=None):
    if self.name == "main":
      return False
    if len(self.args) == 0 or (arg_limit is not None and len(self.args) > arg_limit):
      return False
    for arg in self.args:
      if not arg.is_valid_arg():
        return False
    if self.ret is None or not self.ret.is_valid_ret():
      return False
    contains_print, contains_scan = self.check_func_io()
    return not contains_scan and len(self.args) < arg_limit

  def get_fuzzable_args(self):
    arg_vals = {
        'int': int_vals,
        'float': float_vals,
        'char': char_vals
    }
    fuzzs = []
    limit = len(self.args) > 1
    for arg in self.args:
      fuzzs.append(arg_vals[arg.type](limit=limit))
    return itertools.product(*fuzzs)


class FuncDefStatCollector(c_ast.NodeVisitor):
  generator = c_generator.CGenerator()

  def __init__(self, i_d, name, source):
    self.id = i_d
    self.name = name
    self.source = source
    self.functions = []

  def visit_FuncDef(self, node):
    func = Function(node.decl.name, FuncDefStatCollector.generator.visit(node))
    func.source_id = self.id
    func.source_name = self.name
    func.source = self.source
    arg_nodes = node.decl.type.args
    if arg_nodes and len(arg_nodes.params) > 0:
      for arg_node in arg_nodes.params:
        arg = Arg.parse(arg_node)
        if arg is not None:
          func.args.append(arg)
    func.ret = Return.parse(node.decl.type.type)
    if node.decl and node.decl.storage and 'static' in node.decl.storage:
      func.is_static = True
    self.functions.append(func)
    return func


def c_extract(i_d, name, source, repeat=True):
  """
  Compile c source code.
  :param i_d: ID of row
  :param name: Name of file
  :param source: "Source code as string"
  :param repeat: If AST parsing has to be repeated.
  :return:
  """
  file_name = cache.create_file_path("temp", name, ext=".c")
  collector = FuncDefStatCollector(i_d, file_name.rsplit("/", 1)[-1], source)
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


def _test_static():
  ast, error = parse_c_file("temp/add.c")
  collector = FuncDefStatCollector(1, 'add', '')
  collector.visit(ast)


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
  _read()
  # _test_static()
  # _test_exception()
  # parse_file('temp/fixdep.c', use_cpp=True, cpp_args=[r'-I%s' % FAKE_LIBS_PATH])
  # _test_child_process()
