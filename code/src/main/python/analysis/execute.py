import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import inspect
import signal
import time
import copy

from analysis.helpers import helper
from analysis.helpers import constants as a_consts
from store import mongo_store
from utils import logger, cache
import properties

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))
DEBUG = False
RE_EVALUATE = False
_ARGUMENT_STORE = None
_FUNCTION_STORE = None


def get_function_store(dataset, is_test=False):
  global _FUNCTION_STORE
  if _FUNCTION_STORE is not None:
    return _FUNCTION_STORE
  if properties.STORE != "mongo":
    raise RuntimeError("Currently supports only mongo store. Not supported for '%s'" % properties.STORE)
  _FUNCTION_STORE = mongo_store.FunctionStore(dataset, is_test=is_test)
  return _FUNCTION_STORE


def get_argument_store(dataset, is_test=False):
  global _ARGUMENT_STORE
  if _ARGUMENT_STORE is not None:
    return _ARGUMENT_STORE
  if properties.STORE != "mongo":
    raise RuntimeError("Currently supports only mongo store. Not supported for '%s'" % properties.STORE)
  _ARGUMENT_STORE = mongo_store.ArgumentStore(dataset, is_test=is_test)
  return _ARGUMENT_STORE


def create_arg_key(arg_type):
  if arg_type.get('is_tuple', False) or arg_type.get('is_dict', False):
    return None
  name = arg_type['name']
  if name == 'ndarray':
    return "(float)@1"
  elif arg_type.get('is_list', False):
    count = 0
    _arg_type = arg_type
    while _arg_type.get('type', None) is not None:
      _arg_type = _arg_type['type']
      count += 1
    family = helper.get_family_name(_arg_type['name'])
    if family is None:
      return None
    return "(%s)@%d" % (family, count)
  else:
    family = helper.get_family_name(name)
    return family


def create_arg_keys(dataset, func, is_test):
  func_name = func.__name__
  arg_types = get_function_store(dataset, is_test).load_function_arg_type(func_name)
  if not arg_types:
    if DEBUG:
      LOGGER.warning("Arg Types not found for '%s'" % func_name)
    return None
  arg_names = helper.get_func_arg_names(func)
  if not arg_names or not arg_types:
    if DEBUG:
      LOGGER.warning("Invalid arg names or arg types")
    return None
  arg_keys = []
  for arg_name in arg_names:
    arg_type = arg_types['types'][arg_name]
    if not arg_type['is_valid']:
      return None
    arg_key = create_arg_key(arg_type)
    if arg_key is None:
      return None
    arg_keys.append(arg_key)
  return arg_keys


def create_func_key(arg_keys):
  if arg_keys is None:
    return None
  return ",".join(arg_keys)


def convert_to_executable_arg(key, val):
  if helper.is_list_key(key):
    arr_key, dimension = helper.parse_list_key(key)
    arr_vals = []
    for i, v in enumerate(val):
      if dimension == 1:
        arr_vals.append(v[0])
      else:
        arr_vals.append(convert_to_executable_arg("(%s)%d" % (arr_key, dimension-1), v))
    return arr_vals
  else:
    return val


def get_function_args(dataset, arg_keys, is_test=False):
  if not arg_keys: return None
  func_key = create_func_key(arg_keys)
  arg_data = get_argument_store(dataset, is_test).load_args(func_key)

  if not arg_data:
    if DEBUG:
      LOGGER.warning("Arguments not found for key: '%s'." % func_key)
    return None
  all_func_args = []
  for row in arg_data['args']:
    func_args = []
    for i, arg_key in enumerate(arg_keys):
      func_args.append(convert_to_executable_arg(arg_key, row[i]))
    all_func_args.append(func_args)
  return all_func_args


"""
Executions
"""


class TimeoutException(Exception):
  pass


def timeout_handler(signum, frame):
  raise TimeoutException


# signal.signal(signal.SIGALRM, timeout_handler)


def evaluate_function(dataset, file_name, func, is_test=False):
  function_store = get_function_store(dataset, is_test=is_test)
  simple_name = helper.get_simple_name(file_name)
  if isinstance(func, basestring):
    func = helper.get_function(file_name, func)
  if func is None:
    return None
  function_name = func.__name__
  LOGGER.info("Processing '%s' ..." % function_name)
  if function_store.exists_py_function(function_name) and not RE_EVALUATE:
    LOGGER.info("Function '%s' from '%s' exists. Returning existing value ..." % (function_name, simple_name))
    return function_store.load_py_function(function_name)
  if function_store.is_invalid_py_function(function_name) and not RE_EVALUATE:
    LOGGER.info("Function '%s' from '%s' exists and is invalid." % (function_name, simple_name))
    return None
  arg_keys = create_arg_keys(dataset, func, is_test)
  arg_data = get_function_args(dataset, arg_keys, is_test)
  if not arg_data:
    LOGGER.warning("Arguments not found for key: '%s'. (Function: '%s'; File: '%s')" %
                   (create_func_key(arg_keys), function_name, simple_name))
    return None
  is_valid = False
  outputs = []
  for i, arg in enumerate(arg_data):
    if DEBUG:
      LOGGER.info("Running for %d of %d args" % (i + 1, len(arg_data)))
    result = execute_function(func, arg)
    if not is_valid and result.get("return", None) is not None:
      is_valid = True
    outputs.append(result)
  if not is_valid:
    LOGGER.warning("Function '%s' from file '%s' is not valid" % (function_name, simple_name))
    function_store.save_failed_py_function({
      "name": function_name,
      "fileName": file_name,
      "dataset": dataset,
      "inputKey": create_func_key(arg_keys)
    })
    return None
  function_data = {
    "name": function_name,
    "fileName": file_name,
    "dataset": dataset,
    "inputKey": create_func_key(arg_keys),
    "outputs": outputs
  }
  LOGGER.info("Processed function '%s' ..." % function_name)
  function_store.save_py_function(function_data)
  return function_data

# signal.signal(signal.SIGALRM, timeout_handler)


def execute_function(func, arg):
  cloned = [copy.deepcopy(x) for x in arg]
  prev_signal = signal.getsignal(signal.SIGALRM)
  signal.signal(signal.SIGALRM, timeout_handler)
  signal.alarm(a_consts.METHOD_WAIT_TIMEOUT)
  duration = a_consts.METHOD_WAIT_TIMEOUT * 1000
  return_variable, error_message = None, None
  try:
    start = time.time()
    return_variable = func(*cloned)
    duration = (time.time() - start) * 1000
  except TimeoutException:
    error_message = "Method timed out after %d seconds" % a_consts.METHOD_WAIT_TIMEOUT
  except Exception as e:
    error_message = e.message
  signal.alarm(0)
  signal.signal(signal.SIGALRM, prev_signal)
  return {
    "return": return_variable,
    "errorMessage": error_message,
    "duration": duration
  }


def execute_file(dataset, file_name):
  sys.path.append(properties.PYTHON_PROJECTS_HOME)
  try:
    n_valids, n_totals = 0, 0
    for func in helper.get_generated_functions(file_name):
      func_name = func.__name__
      valid, func_key = is_executable_function(dataset, func, False)
      print(func.__name__, valid)
      n_totals += 1
      if valid:
        evaluated = evaluate_function(dataset, file_name, func_name)
        if evaluated is not None:
          n_valids += 1
    LOGGER.info("Valid Functions: %d / %d" % (n_valids, n_totals))
  except Exception as e:
    LOGGER.critical("Failed to process file: %s. Message: %s" % (file_name, e.message))
  finally:
    sys.path.remove(properties.PYTHON_PROJECTS_HOME)


def execute_problem(dataset, problem_id=None):
  root_folder = os.path.join(properties.PYTHON_PROJECTS_HOME, dataset)
  if problem_id:
    root_folder = os.path.join(root_folder, problem_id)
  for file_path in cache.list_files(root_folder, check_nest=True, is_absolute=True):
    if not cache.get_file_name(file_path).startswith(a_consts.GENERATED_PREFIX):
      continue
    LOGGER.info("Processing '%s'" % helper.get_simple_name(file_path))
    execute_file(dataset, file_path)


"""
Validity
"""


def is_executable_function(dataset, func, is_test):
  arg_keys = create_arg_keys(dataset, func, is_test)
  func_key = create_func_key(arg_keys)
  args = get_function_args(dataset, arg_keys, is_test)
  if args is None:
    return False, func_key
  return True, func_key


def get_valid_function_keys_from_file(dataset, file_name):
  sys.path.append(properties.PYTHON_PROJECTS_HOME)
  valid_keys = []
  n_generated_functions = 0
  for func in helper.get_generated_functions(file_name):
    n_generated_functions += 1
    valid, func_key = is_executable_function(dataset, func, True)
    if valid:
      valid_keys.append(func_key)
  sys.path.remove(properties.PYTHON_PROJECTS_HOME)
  return valid_keys, n_generated_functions


def get_valid_functions_from_folder(dataset, problem_id=None):
  total_valid_functions = 0
  accessed_keys = set()
  root_folder = properties.PYTHON_PROJECTS_HOME
  if problem_id:
    root_folder = os.path.join(root_folder, problem_id)
  for file_path in cache.list_files(root_folder, check_nest=True, is_absolute=True):

    file_name = cache.get_file_name(file_path)
    if not file_name.startswith(a_consts.GENERATED_PREFIX):
      continue
    LOGGER.info("Processing '%s'" % helper.get_simple_name(file_path))
    valid_keys, n_generated_functions = get_valid_function_keys_from_file(dataset, file_path)
    LOGGER.info("Valid Functions: %d / %d\n" % (len(valid_keys), n_generated_functions))
    accessed_keys.update(valid_keys)
    total_valid_functions += len(valid_keys)
  LOGGER.info("Total valid functions: %d" % total_valid_functions)
  print(accessed_keys)


"""
Metadata
"""


def extract_metadata_for_folder(dataset, problem_id=None):
  sys.path.append(properties.PYTHON_PROJECTS_HOME)
  function_store = get_function_store(dataset)
  root_folder = os.path.join(properties.PYTHON_PROJECTS_HOME, dataset)
  if problem_id:
    root_folder = os.path.join(root_folder, problem_id)
  for file_path in cache.list_files(root_folder, check_nest=True, is_absolute=True):
    file_name = cache.get_file_name(file_path)
    if not file_name.startswith(a_consts.GENERATED_PREFIX):
      continue
    LOGGER.info("Processing '%s' ..." % helper.get_simple_name(file_path))
    for func in helper.get_generated_functions(file_path):
      function_name = func.__name__
      valid, func_key = is_executable_function(dataset, func, False)
      print(function_name, func_key, valid)
      if valid:
        meta_data = {
          "name": function_name,
          "body": inspect.getsource(func),
          "inputKey": func_key,
          "filePath": file_path
        }
        function_store.save_py_metadata(meta_data)
  sys.path.remove(properties.PYTHON_PROJECTS_HOME)


"""
Re-execute functions
"""


def reexecute_functions(dataset):
  sys.path.append(properties.PYTHON_PROJECTS_HOME)
  function_store = get_function_store(dataset, is_test=True)
  argument_store = get_argument_store(dataset, is_test=True)
  function_names = function_store.get_executed_functions("python")
  for func_name in function_names:
    try:
      file_path = function_store.load_py_metadata(func_name)["filePath"]
      if not file_path or function_store.exists_py_function(func_name):
        continue
      evaluate_function(dataset, file_path, func_name, is_test=True)
    except Exception:
      pass
  sys.path.remove(properties.PYTHON_PROJECTS_HOME)


if __name__ == "__main__":
  store = get_function_store("codejam", is_test=False)
  # execute_file("codejam", "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/python/Y11R5P1/falcon/generated_py_0b8135888969475c9b0f67b3e22fb7c5.py")
  # get_valid_functions_from_folder("codejam")
  # print(get_function_args("codejam", ["int", "(int)@1"])[0])