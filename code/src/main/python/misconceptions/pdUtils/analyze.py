import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import ast
import astor
import asttokens
import inspect
from collections import Counter
import warnings

from analysis.helpers import helper
from analysis import execute
from utils import logger, cache
from analysis.parsers import parser
from misconceptions.common import props, mongo_driver, arg_generator
from misconceptions.pdUtils import crawler

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))
_PY_CONSTANTS = None
DEBUG = False
TEMP_FUNC_PATH = os.path.join(props.MISCONCEPTIONS_HOME, "temp_func_file.py")
warnings.filterwarnings("ignore")


def get_default_function_names():
  global _PY_CONSTANTS
  if _PY_CONSTANTS:
    return _PY_CONSTANTS
  constant_libs = ["np", "pd", "numpy", "pandas"]
  module = inspect.getmodule(abs)
  _PY_CONSTANTS = set(dir(module))
  _PY_CONSTANTS.update(constant_libs)
  return _PY_CONSTANTS


class VariableDetector(parser.Traveller):
  def __init__(self, src):
    self.src = src
    self.ast_tokenized = None
    self.variable_names = set()
    self.ignores = set()
    parser.Traveller.__init__(self)

  def parse(self):
    self.ast_tokenized = asttokens.ASTTokens(self.src, parse=True)
    self.visit(self.ast_tokenized.tree)
    return self.variable_names - self.ignores

  def visit_Name(self, node, meta):
    var_name = node.id
    if var_name not in get_default_function_names() and var_name not in self.ignores:
      self.variable_names.add(var_name)

  def visit_Lambda(self, node, meta):
    if node.args and node.args.args:
      for arg in node.args.args:
        arg_name = arg.id
        self.ignores.add(arg_name)
    self.visit(node.body, meta)


def get_return_values(stmt):
  rets = []
  ast_tokenized = asttokens.ASTTokens(stmt, parse=True)
  parsed_stmt = ast_tokenized.tree.body[0]
  if isinstance(parsed_stmt, ast.Assign):
    for target in parsed_stmt.targets:
      rets.append(ast_tokenized.get_text(target))
  elif isinstance(parsed_stmt, ast.AugAssign):
    rets.append(ast_tokenized.get_text(parsed_stmt.target))
  elif isinstance(parsed_stmt, ast.Return):
    rets = props.AUTO_RETURN
  else:
    rets = props.SELF
  return rets


def extract_variable_names():
  store = mongo_driver.MongoStore(props.DATASET)
  docs = store.load_file_stmts(props.TYPE_PYTHON)
  stored_stmts = store.load_stmts(props.TYPE_PYTHON, is_valid=False)
  stmt_counter = Counter()
  for i, doc in enumerate(docs):
    for stmt in doc['snippets']:
      if not stored_stmts or (stmt, props.TYPE_PYTHON) not in stored_stmts:
        stmt_counter[stmt] = stmt_counter.get(stmt, 0) + 1
  valid_stmts = 0
  for i, (stmt, count) in enumerate(stmt_counter.items()):
    if i % 1000 == 0:
      LOGGER.info("Processing %d / %d .... " % (i + 1, len(stmt_counter)))
    try:
      detector = VariableDetector(stmt)
      variables = list(detector.parse())
      if len(variables) == 1:
        valid_stmts += 1
      else:
        variables = None
        if DEBUG:
          LOGGER.info(list(variables))
          LOGGER.info("STMT:::: %s\n" % stmt)
    except Exception:
      variables = None
      if DEBUG:
        LOGGER.info(list(variables))
        LOGGER.info("EXCEPTION::::  %s\n" % stmt)
    store.store_stmt(stmt, props.TYPE_PYTHON, variables)
  LOGGER.info("VALID: %d / %d" % (valid_stmts, len(stmt_counter)))


def as_nodes(stmts):
  try:
    tokenized = asttokens.ASTTokens("\n".join(map(str, stmts)), parse=True)
  except Exception:
    print(stmts)
    # raise RuntimeError("Failed to handle stmts\n", e)
    return None
  return tokenized.tree.body


def create_temp_function_file(variable, body):
  headers = "\n".join(["import numpy", "import pandas", "np, pd = numpy, pandas"])
  file_path = os.path.join(props.MISCONCEPTIONS_HOME, "temp_func_%s.py" % helper.generate_random_string()[:6])
  func_name = helper.generate_function_name()
  args = ast.arguments(args=[ast.Name(id=str(variable))], vararg=None, kwarg=None, defaults=[])
  func_node = ast.FunctionDef(name=func_name, args=args, body=as_nodes(body), decorator_list=[])
  if func_node is None:
    return None
  func_str = astor.to_source(func_node)
  content = "\n\n".join([headers, func_str])
  cache.write_file(file_path, content)
  if helper.is_valid_file(file_path, props.PYTHON_SRC):
    return func_name, file_path
  cache.delete_file(file_path)
  return None, file_path


def strip_comments(code):
  tree = ast.parse(code)
  return astor.to_source(tree).strip()


def execute_stmt(stmt, args):
  snippet = strip_comments(stmt['snippet'])
  rets = get_return_values(snippet)
  inp = stmt['variables'][0]
  ret_bodies = {}
  if rets == props.SELF:
    ret_bodies[props.SELF] = ["return %s" % snippet]
  elif rets == props.AUTO_RETURN:
    ret_bodies[props.AUTO_RETURN] = [snippet]
  else:
    for ret in rets:
      ret_bodies[ret] = [snippet, "return %s" % ret]
  ret_results = {}
  for ret, body in ret_bodies.items():
    func_name, file_path = create_temp_function_file(inp, body)
    if func_name is None:
      cache.delete_file(file_path)
      continue
    func = helper.get_function(file_path, func_name, props.PYTHON_SRC)
    assert func is not None
    results = []
    for arg_set in args:
      result = execute.execute_function(func, arg_set)
      try:
        result['return'] = mongo_driver.to_mongo_format(result['return'])
      except Exception as e:
        result['return'] = None
        result['errorMessage'] = e.message
      results.append(result)
    cache.delete_file(file_path)
    ret_results[mongo_driver.mongo_escape(ret)] = results
  return ret_results


def execute_stmts(stmts, limit=props.PY_STMT_LIMIT, do_log=False):
  store = mongo_driver.MongoStore(props.DATASET)
  n_stmts = len(stmts)
  top_py_stmts = crawler.get_stmt_counts(limit)
  valids = 0
  generated_args = arg_generator.generate_args()
  for i, (key, stmt) in enumerate(stmts.items()):
    snippet = stmt["snippet"]
    if snippet not in top_py_stmts:
      if do_log: LOGGER.info("Not processing %d / %d. Moving on !" % (i + 1, n_stmts))
      continue
    if 'outputs' in stmt:
      LOGGER.info("Processed %d / %d. Moving on !" % (i + 1, n_stmts))
      continue
    # To skip plotting functions.
    if ".hist(" in snippet:
      LOGGER.info("Snippet %d / %d contains a plot operation. Moving on !" % (i + 1, n_stmts))
      continue
    LOGGER.info("Processing %d / %d .... " % (i + 1, n_stmts))
    outputs = execute_stmt(stmt, generated_args)
    assert len(outputs) > 0
    store.update_stmt_outputs(stmt['_id'], outputs)
    valids += 1
  LOGGER.info("Valid outputs = %d / %d" % (valids, n_stmts))


def run_execute_stmts():
  store = mongo_driver.MongoStore(props.DATASET)
  stmts = store.load_stmts(language="py", is_valid=True)
  execute_stmts(stmts, do_log=False)


def test_execute_stmts():
  store = mongo_driver.MongoStore(props.DATASET)
  ids = ["5cafff91e850c97e6a1f5b9c","5cafff91e850c97e6a1f5b9e","5cafff91e850c97e6a1f5b9f","5cafff91e850c97e6a1f5ba0","5cafff91e850c97e6a1f5ba5","5cafff91e850c97e6a1f5bb0","5cafff91e850c97e6a1f5bb7","5cafff91e850c97e6a1f5bc6","5cafff91e850c97e6a1f5bc8","5cafff91e850c97e6a1f5bf0"]
  stmts = {stmt["_id"]: stmt for stmt in [store.load_stmt(_id) for _id in ids]}
  execute_stmts(stmts)


def _test_import():
  print(helper.is_valid_file(TEMP_FUNC_PATH, props.PYTHON_SRC))


def _test():
  src = "x += train_df.head()"
  print(get_return_values(src))
  src = "dataset['Title'] = dataset['Title'].replace('Mme', 'Mrs')"
  print(get_return_values(src))
  src = "test_df[\"t_has_prefix\"] = test_df['Ticket'].apply(lambda x: 1 if len(x.split())>1 else 0)"
  print(get_return_values(src))
  print(strip_comments("train_df.head('#123')  # Hello World"))


def _test_execute_stmt():
  store = mongo_driver.MongoStore(props.DATASET)
  generated_args = arg_generator.generate_args()
  stmt = store.load_stmt("5cafff91e850c97e6a1f5b9c")
  print(execute_stmt(stmt, generated_args).values()[0][0])


if __name__ == "__main__":
  # extract_variable_names()
  # test_execute_stmts()
  run_execute_stmts()

