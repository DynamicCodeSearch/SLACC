import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import pandas as pd
import re
from collections import OrderedDict

from analysis.helpers import helper
from analysis import execute
from misconceptions.common import datatypes
from misconceptions.rUtils import generator
from utils import cache

FUNCTION_STORE = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/src/main/python/expt/pd_functions.pkl"


def get_pd_functions(file_path, as_dict=False):
  return helper.get_generated_functions(file_path, as_dict=as_dict)


def get_pd_types(pd_func):
  # TODO: need to create a meta folder
  arg_types = OrderedDict()
  for arg_name in helper.get_func_arg_names(pd_func):
    arg_types[arg_name] = {"type": pd.core.frame.DataFrame}
  return arg_types


def execute_pd_function_on_args(pd_func, args_set):
  results = []
  is_valid = False
  for arg_set in args_set:
    result = execute.execute_function(pd_func, arg_set)
    if not is_valid and result.get("return", None) is not None:
      is_valid = True
    results.append(result)
  if not is_valid:
    print("Function is invalid")
    return None
  return results


def process_pd_function(file_path, pd_func):
  print("Processing %s ... " % pd_func.__name__)
  pd_types = get_pd_types(pd_func)
  if pd_types is None:
    return None
  args = generator.load_args(pd_types)
  results = execute_pd_function_on_args(pd_func, args)
  func_key = generator.make_key(pd_types)
  function_data = {
    "name": pd_func.__name__,
    "filePath": file_path,
    "inputKey": func_key,
    "body": helper.get_func_body(pd_func)
  }
  if results:
    function_data["outputs"] = results
  return function_data


def save_function(func_data):
  saved_funcs = cache.load_pickle(FUNCTION_STORE)
  if not saved_funcs:
    saved_funcs = {}
  saved_funcs[func_data["name"]] = func_data
  cache.save_pickle(FUNCTION_STORE, saved_funcs)


def extract_col_names(arg_name, func_body):
  COL_NAME_REGEX = r"[\'\"](.*?)[\'\"]"
  # print(re.findall(COL_NAME_REGEX, '"Hello orl"  \'assad\''))
  DIRECT_ACCESS = r'%s\[\[%s(?:\s*?,\s*?%s)*\]\]' % (arg_name, COL_NAME_REGEX, COL_NAME_REGEX)
  LOC_ACCESS = r'%s\.loc\[.*?\s*,\s*%s(?:\s*?\:\s*?%s)*\]' % (arg_name, COL_NAME_REGEX, COL_NAME_REGEX)
  x = re.findall(DIRECT_ACCESS, func_body)
  y = re.findall(LOC_ACCESS, func_body)
  col_names = set()
  for group in x + y:
    for col_name in list(group):
      if col_name and col_name.strip():
        col_names.add(col_name)
  if col_names:
    df = datatypes.DataFrame()
    df.name = arg_name
    df.columns = {}
    for name in sorted(list(col_names)):
      column = datatypes.Series()
      column.name = name
      df.columns[name] = column
    return df
  return None


def parse_function_for_col_names(func_name, source_file):
  all_funcs = get_pd_functions(source_file, as_dict=True)
  pd_func = all_funcs[func_name]
  arg_names = helper.get_func_arg_names(pd_func)
  func_body = helper.get_func_body(pd_func)
  arg_cols = {}
  for arg_name in arg_names:
    df = extract_col_names(arg_name, func_body)
    if df:
      arg_cols[arg_name] = df
  return arg_cols
