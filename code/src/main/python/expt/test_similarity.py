import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


from utils import cache, logger, lib, stat
from analysis import execute
from analysis.helpers import helper
from misconceptions.rUtils import generator, functions as r_functions
from misconceptions.pdUtils import functions as pd_functions
from sos.function import Function, Outputs
from expt import test_R, test_pd, test_clustering


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))
PD_FUNCTIONS_SOURCE_FILE = "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/python/Example/PandasR/generated_py_d123.py"
R_FUNCTIONS_SOURCE_FILE = "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/R/Example/PandasR/r_snippets.R"
BASE_CLUSTER_FOLDER = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/src/main/python/expt"


def process_R_function(file_path, func_name, r_func):
  print("Processing %s ... " % func_name)
  r_types = r_functions.get_r_types(r_func)
  if r_types is None:
    return None
  r_func_arg_cols = r_functions.parse_function_for_col_names(func_name, file_path)
  for name, props in r_types.items():
    if name in r_func_arg_cols:
      props['col_names'] = r_func_arg_cols[name].columns
  func_key = generator.make_key(r_types)
  args = generator.load_args(r_types)
  results = []
  is_valid = False
  for arg in args:
    result = r_functions.execute_R_function(r_func, arg)
    if not is_valid and result.get("return", None) is not None:
      is_valid = True
    results.append(result)
  function_data = {
    "name": func_name,
    "filePath": file_path,
    "inputKey": func_key,
    "body": r_functions.get_function_as_str(func_name, r_func)
  }
  if is_valid:
    function_data["outputs"] = results
  return function_data


def process_pd_function(file_path, pd_func):
  print("Processing %s ... " % pd_func.__name__)
  pd_types = pd_functions.get_pd_types(pd_func)
  if pd_types is None:
    return None
  py_func_arg_cols = pd_functions.parse_function_for_col_names(pd_func.__name__, PD_FUNCTIONS_SOURCE_FILE)
  for name, props in pd_types.items():
    if name in py_func_arg_cols:
      props['col_names'] = py_func_arg_cols[name].columns
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


def similarity(r_func_name, py_func_name):
  r_func = r_functions.get_r_functions(R_FUNCTIONS_SOURCE_FILE)[r_func_name]
  pd_func = pd_functions.get_pd_functions(PD_FUNCTIONS_SOURCE_FILE, as_dict=True)[py_func_name]
  r_executed = process_R_function(R_FUNCTIONS_SOURCE_FILE, r_func_name, r_func)
  r_func = Function(name=r_func_name, input_key=r_executed["inputKey"],
                    outputs=Outputs(r_executed["outputs"]),
                    body=test_clustering.get_body(r_executed), source=R_FUNCTIONS_SOURCE_FILE)
  pd_executed = process_pd_function(PD_FUNCTIONS_SOURCE_FILE, pd_func)
  pd_func = Function(name=py_func_name, input_key=pd_executed["inputKey"],
                     outputs=Outputs(pd_executed["outputs"]),
                     body=test_clustering.get_body(pd_executed), source=PD_FUNCTIONS_SOURCE_FILE)
  print(test_clustering.execution_similarity(r_func, pd_func))


def _similarity():
  r_func_name = "gen_func_r_distinct1"
  py_func_name = "func_py_distinct1"
  similarity(r_func_name, py_func_name)


if __name__ == "__main__":
  _similarity()
