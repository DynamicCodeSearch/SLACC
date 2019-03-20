import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import pandas as pd

from analysis.helpers import helper
from analysis import execute
from sos.rUtils import generator
from utils import cache


FUNCTION_STORE = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/src/main/python/expt/pd_functions.pkl"


def get_pd_functions(file_path):
  return helper.get_generated_functions(file_path)


def get_pd_types(pd_func):
  # TODO: need to create a meta folder
  arg_types = []
  for _ in helper.get_func_arg_names(pd_func):
    arg_types.append(pd.core.frame.DataFrame)
  return arg_types


def process_pd_function(file_path, pd_func):
  print("Processing %s ... " % pd_func.__name__)
  pd_types = get_pd_types(pd_func)
  if pd_types is None:
    return None
  args = generator.load_args(pd_types)
  func_key = generator.make_key(pd_types)
  results = []
  is_valid = False
  for arg_set in args:
    result = execute.execute_function(pd_func, arg_set)
    if not is_valid and result.get("return", None) is not None:
      is_valid = True
    results.append(result)
  function_data = {
    "name": pd_func.__name__,
    "filePath": file_path,
    "inputKey": func_key,
    "body": helper.get_func_body(pd_func)
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


def process_file(file_path):
  pd_functions = get_pd_functions(file_path)
  n_valid = 0
  print("Processing %d functions from '%s' ... " % (len(pd_functions), file_path))
  for pd_func in pd_functions:
    evaluated = process_pd_function(file_path, pd_func)
    if evaluated is not None and "outputs" in evaluated:
      n_valid += 1
      save_function(evaluated)
  print("Valid functions: %d/%d" % (n_valid, len(pd_functions)))


if __name__ == "__main__":
  process_file("/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/python/Example/PandasR/generated_py_d123.py")
