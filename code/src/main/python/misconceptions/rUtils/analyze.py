import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from collections import Counter
import rpy2
import rpy2.robjects as robjects
from rpy2 import rinterface

from analysis.helpers import helper
from utils import logger, cache
from misconceptions.common import props, mongo_driver, arg_generator, datatypes
from misconceptions.rUtils import functions


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))
R_PARSER_PATH = os.path.join(props.CODE_SRC, "r", "parser", "r_parser.R")
DEBUG = False
R_SUPPORTED_LIBRARIES = ['base', 'dplyr', 'stats']
TEMP_FUNC_PATH = os.path.join(props.MISCONCEPTIONS_HOME, "temp_func_file.R")

_FIND_VAR_FUNC = None
_FIND_ASSIGN = None


def get_find_var_func():
  global _FIND_VAR_FUNC
  if not _FIND_VAR_FUNC:
    _FIND_VAR_FUNC = functions.get_r_function(R_PARSER_PATH, "find_vars")
  return _FIND_VAR_FUNC


def get_find_assign():
  global _FIND_ASSIGN
  if not _FIND_ASSIGN:
    _FIND_ASSIGN = functions.get_r_function(R_PARSER_PATH, "find_assign")
  return _FIND_ASSIGN


def extract_variable(expr):
  r_func = get_find_var_func()
  try:
    x = datatypes.convert_r_object_to_py(r_func(expr)).tolist()
    return x
  except rinterface.RRuntimeError:
    return None


def get_return_variable(expr):
  cleaned_expr = expr.replace(" = ", " <- ", 1)
  r_func = get_find_assign()
  try:
    x = datatypes.convert_r_object_to_py(r_func(cleaned_expr))
    if len(x) == 1:
      return str(x[0])
    return props.AUTO_RETURN
  except rinterface.RRuntimeError as e:
    return None


def extract_variable_names():
  store = mongo_driver.MongoStore(props.DATASET)
  docs = store.load_file_stmts(props.TYPE_R)
  stored_stmts = store.load_stmts(props.TYPE_R, is_valid=False)
  stmt_counter = Counter()
  for i, doc in enumerate(docs):
    for stmt in doc['snippets']:
      if not stored_stmts or (stmt, props.TYPE_R) not in stored_stmts:
        stmt_counter[stmt] = stmt_counter.get(stmt, 0) + 1
  valid_stmts = 0
  for i, (stmt, count) in enumerate(stmt_counter.items()):
    if i % 10 == 0:
      LOGGER.info("Processing %d / %d .... " % (i + 1, len(stmt_counter)))
    variables = extract_variable(stmt)
    if variables and len(variables) == 1:
      valid_stmts += 1
    else:
      variables = None
      if DEBUG:
        LOGGER.info(list(variables))
        LOGGER.info("STMT:::: %s\n" % stmt)
    store.store_stmt(stmt, props.TYPE_R, variables)
  LOGGER.info("VALID: %d / %d" % (valid_stmts, len(stmt_counter)))


def create_temp_function(variable, body):
  headers = "\n".join(['library("%s")' % header for header in R_SUPPORTED_LIBRARIES])
  func_name = helper.generate_function_name()
  func_source = """
%s <- function (%s) {
  %s
}
  """ % (func_name, variable, body)
  file_source = "\n\n".join([headers, func_source, ""])
  cache.write_file(TEMP_FUNC_PATH, file_source.encode('utf-8'))
  r_func = functions.get_r_function(TEMP_FUNC_PATH, func_name)
  return r_func


def execute_stmt(stmt, args):
  snippet = stmt['snippet'].strip()
  ret = get_return_variable(snippet)
  inp = stmt['variables'][0]
  body = None
  if ret == props.AUTO_RETURN:
    body = snippet
  elif ret is not None:
    body = "\n  ".join([snippet, ret])
  ret_results = {}
  if body:
    r_func = create_temp_function(inp, body)
    results = []
    if r_func is not None:
      for arg_set in args:
        result = functions.execute_R_function(r_func, arg_set)
        # if result and result['return'] is not None:
        #   print(result)
        #   exit()
        result['return'] = mongo_driver.to_mongo_format(result['return'])
        results.append(result)
    ret_results[mongo_driver.mongo_escape(ret)] = results
    cache.delete_file(TEMP_FUNC_PATH)
  return ret_results


def execute_stmts():
  store = mongo_driver.MongoStore(props.DATASET)
  generated_args = arg_generator.generate_args()
  stmts = store.load_stmts(language='R')
  n_stmts = len(stmts)
  for i, (key, stmt) in enumerate(stmts.items()):
    if 'outputs' in stmt:
      LOGGER.info("Processing %d / %d. Moving on ... " % (i + 1, n_stmts))
      continue
    LOGGER.info("StmtID : '%s'. Processing %d / %d .... " % (stmt['_id'], i + 1, n_stmts))
    outputs = execute_stmt(stmt, generated_args)
    store.update_stmt_outputs(stmt['_id'], outputs)


def run_execute_stmts():
  execute_stmts()

def _main():
  # extract_variable_names()
  execute_stmts()


def _test():
  print(extract_variable('qwe <- table(hello$bbc == common, two)'))
  print(extract_variable('\"x\"'))
  print(get_return_variable('table(hello$bbc == common, two)'))


if __name__ == "__main__":
  execute_stmts()
  # _test()
  # _main()
