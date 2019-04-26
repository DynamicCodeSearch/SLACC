import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


import copy
import signal
import time
import re
import rpy2
import rpy2.robjects as robjects
from rpy2 import rinterface
from rpy2.robjects import pandas2ri
from rpy2.robjects.functions import SignatureTranslatedFunction
from collections import OrderedDict


from analysis.helpers import constants as a_consts
from analysis import execute
from misconceptions.common import datatypes
from misconceptions.rUtils import generator, dataframer
from utils import cache

pandas2ri.activate()
rinterface.set_writeconsole_warnerror(None)
rinterface.set_writeconsole_regular(None)
r_source = robjects.r['source']

R_GEN_PREFIX = "gen_func_r_"
FUNC_BODY_REGEX = r'function\s*\(.*?\)\s*((.|\s)+)'
FUNCTION_STORE = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/src/main/python/expt/r_functions.pkl"


def get_R_error_message(exception):
  return exception.message.strip()


def get_env_variables(r_file_path):
  try:
    robjects.r('''
      source('%s')
    ''' % r_file_path)
    return robjects.globalenv
  except rinterface.RRuntimeError as e:
    print("Error while fetching environment variables.\n%s" % get_R_error_message(e))
  return None


def r_compile(r_file_path, del_compiled=True):
  try:
    robjects.r('''
      library(compiler)
      cmpfile('%s')
    ''' % r_file_path)
    if del_compiled:
      compiled_file = r_file_path.rsplit(".", 1)[0] + ".Rc"
      cache.delete_file(compiled_file)
    return True
  except Exception as e:
    # print("Error while compilation.\n%s" % get_R_error_message(e))
    # error_message = get_R_error_message(e)
    # return error_message and "import pandas" in error_message
    pass
  return False


def get_r_function(r_file_path, func_name):
  env_variables = get_env_variables(r_file_path)
  if not env_variables:
    return None
  for name in env_variables.keys():
    if name == func_name and isinstance(env_variables[name], SignatureTranslatedFunction):
      return env_variables[name]
  return None


def get_r_functions(r_file_path):
  r_functions = {}
  env_variables = get_env_variables(r_file_path)
  if not env_variables:
    return None
  for name in env_variables.keys():
    if isinstance(env_variables[name], SignatureTranslatedFunction):
      r_functions[name] = env_variables[name]
  return r_functions


def get_function_arg_names(r_func):
  return list(r_func.formals().names)


def get_function_body(r_func):
  func_str = str(r_func).strip()
  return re.match(FUNC_BODY_REGEX, func_str).group(1)


def get_r_types(r_func):
  formal_args = r_func.formals()
  arg_names = get_function_arg_names(r_func)
  if formal_args is None or type(formal_args) == rpy2.rinterface.RNULLType:
    return None
  r_types = OrderedDict()
  for arg_name, formal_arg in zip(arg_names, formal_args):
    r_types[arg_name] = {"type": rpy2.robjects.vectors.DataFrame}
  return r_types


def get_function_as_str(func_name, func):
  return ("%s <- %s" % (func_name, str(func))).strip()


def convert_to_R_args(py_args):
  r_args = []
  for py_arg in py_args:
    r_arg = datatypes.convert_py_object_to_r(py_arg)
    r_args.append(r_arg)
  return r_args


def execute_R_function(r_func, arg):
  cloned = convert_to_R_args([copy.deepcopy(x) for x in arg])
  prev_signal = signal.getsignal(signal.SIGALRM)
  signal.signal(signal.SIGALRM, execute.timeout_handler)
  signal.alarm(a_consts.METHOD_WAIT_TIMEOUT)
  duration = a_consts.METHOD_WAIT_TIMEOUT * 1000
  ret_obj = {"return": None, "errorMessage": None}
  try:
    start = time.time()
    ret = r_func(*cloned)
    duration = (time.time() - start) * 1000
    ret_obj["return"] = datatypes.convert_r_object_to_py(ret)
  except execute.TimeoutException:
    ret_obj["errorMessage"] = "Method timed out after %d seconds" % a_consts.METHOD_WAIT_TIMEOUT
  except rinterface.RRuntimeError as e:
    # print("Error while executing rUtils function %s. Error: %s" % (func_name, e.message))
    ret_obj["errorMessage"] = e.message
  except Exception as e:
    ret_obj["errorMessage"] = e.message
  ret_obj["duration"] = duration
  signal.alarm(0)
  signal.signal(signal.SIGALRM, prev_signal)
  return ret_obj


def process_R_function(file_path, func_name, r_func):
  print("Processing %s ... " % func_name)
  r_types = get_r_types(r_func)
  if r_types is None:
    return None
  args = generator.load_args(r_types)
  func_key = generator.make_key(r_types)
  results = execute_R_function_on_args(r_func, args)
  function_data = {
    "name": func_name,
    "filePath": file_path,
    "inputKey": func_key,
    "body": get_function_as_str(func_name, r_func)
  }
  if results:
    function_data["outputs"] = results
  return function_data


def execute_R_function_on_args(r_func, args_set):
  results = []
  is_valid = False
  for args in args_set:
    result = execute_R_function(r_func, args)
    if not is_valid and result.get("return", None) is not None:
      is_valid = True
    results.append(result)
  if not is_valid:
    print("Function is invalid")
    return None
  return results


def save_function(func_data):
  saved_funcs = cache.load_pickle(FUNCTION_STORE)
  if not saved_funcs:
    saved_funcs = {}
  saved_funcs[func_data["name"]] = func_data
  cache.save_pickle(FUNCTION_STORE, saved_funcs)


def extract_col_names(r_func):
  arg_names = get_function_arg_names(r_func)
  func_body = get_function_body(r_func)
  arg_cols = {}
  for arg_name in arg_names:
    df = dataframer.extract_col_names(arg_name, func_body)
    if df:
      arg_cols[arg_name] = df
  return arg_cols


def parse_function_for_col_names(func_name, source_file):
  all_funcs = get_r_functions(source_file)
  r_func = all_funcs[func_name]
  return extract_col_names(r_func)


def test_function():
  file_path = '/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/R/Example/PandasR/r_snippets.R'
  func_name = 'gen_func_r_drop'
  r_functions = get_r_functions(file_path)
  r_func = r_functions[func_name]
  process_R_function(file_path, func_name, r_func)
