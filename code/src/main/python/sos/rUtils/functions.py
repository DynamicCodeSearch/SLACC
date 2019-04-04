import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


import signal
import time
import re
import rpy2
import rpy2.robjects as robjects
from rpy2 import rinterface
from rpy2.robjects import pandas2ri
from collections import OrderedDict


from analysis.helpers import constants as a_consts
from analysis import execute
from sos.rUtils import generator, dataframer
from utils import cache

pandas2ri.activate()
rinterface.set_writeconsole_warnerror(None)
r_source = robjects.r['source']

R_GEN_PREFIX = "gen_func_r_"
FUNC_BODY_REGEX = r'function\s*\(.*?\)\s*((.|\s)+)'
FUNCTION_STORE = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/src/main/python/expt/r_functions.pkl"


def get_R_error_message(exception):
  return exception.message.strip()


def get_r_functions(r_file_path):
  r_functions = {}
  try:
    robjects.r('''
      source('%s')
    ''' % r_file_path)
    for name in robjects.globalenv.keys():
      if name.startswith(R_GEN_PREFIX):
        # print(type(func_obj))
        # print(func_obj.formals())  ## Fetch function formal arg names
        r_functions[name] = robjects.globalenv[name]
  except rinterface.RRuntimeError as e:
    print("Error while fetching rUtils functions : %s" % get_R_error_message(e))
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
    r_arg = generator.convert_py_object_to_r(py_arg)
    r_args.append(r_arg)
  return r_args


def execute_R_function(r_func, arg):
  prev_signal = signal.getsignal(signal.SIGALRM)
  signal.signal(signal.SIGALRM, execute.timeout_handler)
  signal.alarm(a_consts.METHOD_WAIT_TIMEOUT)
  duration = a_consts.METHOD_WAIT_TIMEOUT * 1000
  ret_obj = {}
  try:
    start = time.time()
    ret = r_func(*arg)
    duration = (time.time() - start) * 1000
    ret_obj["return"] = generator.convert_r_object_to_py(ret)
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
  results = []
  is_valid = False
  for arg in args:
    r_arg = convert_to_R_args(arg)
    result = execute_R_function(r_func, r_arg)
    if not is_valid and result.get("return", None) is not None:
      is_valid = True
    results.append(result)
  function_data = {
    "name": func_name,
    "filePath": file_path,
    "inputKey": func_key,
    "body": get_function_as_str(func_name, r_func)
  }
  if is_valid:
    function_data["outputs"] = results
  return function_data


def save_function(func_data):
  saved_funcs = cache.load_pickle(FUNCTION_STORE)
  if not saved_funcs:
    saved_funcs = {}
  saved_funcs[func_data["name"]] = func_data
  cache.save_pickle(FUNCTION_STORE, saved_funcs)


def parse_function_for_col_names(func_name, source_file):
  all_funcs = get_r_functions(source_file)
  r_func = all_funcs[func_name]
  arg_names = get_function_arg_names(r_func)
  func_body = get_function_body(r_func)
  arg_cols = {}
  for arg_name in arg_names:
    col_names = dataframer.extract_col_names(arg_name, func_body)
    arg_cols[arg_name] = col_names
  return arg_cols


def test_function():
  file_path = '/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/R/Example/PandasR/r_snippets.R'
  func_name = 'gen_func_r_drop'
  r_functions = get_r_functions(file_path)
  r_func = r_functions[func_name]
  process_R_function(file_path, func_name, r_func)
