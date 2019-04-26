import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from collections import OrderedDict
from misconceptions.rUtils import functions as r_functions, datatypes, generator, dataframer
from misconceptions.pdUtils import functions as pd_functions
from sos.function import Function, Outputs
from analysis.helpers import helper
from expt import test_clustering

r_source_file = '/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/R/Example/PandasR/r_snippets.R'
pd_source_file = '/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/python/Example/PandasR/generated_py_d123.py'
ARGS_FILE = '/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/R/Example/PandasR/arg_example.R'


def get_sample_args(arg_names):
  sample_args = {}
  env_variables = r_functions.get_env_variables(ARGS_FILE)
  if not env_variables:
    return sample_args
  for arg_name in arg_names:
    sample_args[arg_name] = env_variables[arg_name]
  return sample_args


def get_generated_args(r_func, n_args):
  arg_names = r_functions.get_function_arg_names(r_func)
  sample_args = get_sample_args(arg_names)
  assert len(arg_names) == len(sample_args)
  extracted_dfs = r_functions.extract_col_names(r_func)
  sample_variables = OrderedDict()
  for name, sample_arg in sample_args.items():
    analyzed_sample_variable = datatypes.analyze_sample_variable(sample_arg)
    analyzed_sample_variable.name = name
    sample_variables[name] = analyzed_sample_variable
  for name, df in extracted_dfs.items():
    if name not in sample_variables:
      continue
    for col_name, column in df.columns.items():
      if col_name not in sample_variables[name].columns:
        sample_variables[name].columns[col_name] = column
  generated_args = generator.generate_args_from_sample(sample_variables, n_args)
  return generated_args


def compare_functions(r_func_name, pd_func_name):
  r_func = r_functions.get_r_function(r_source_file, r_func_name)
  pd_func = pd_functions.get_pd_functions(pd_source_file, as_dict=True)[pd_func_name]
  generated_args = get_generated_args(r_func, 100)
  r_results = r_functions.execute_R_function_on_args(r_func, generated_args)
  r_executed = {
    "name": r_func_name,
    "body": r_functions.get_function_body(r_func),
    "inputKey": "DF-KEY",
    "outputs": r_results
  }
  pd_results = pd_functions.execute_pd_function_on_args(pd_func, generated_args)
  pd_executed = {
    "name": pd_func_name,
    "body": helper.get_func_body(pd_func),
    "inputKey": "DF-KEY",
    "outputs": pd_results
  }
  r_func = Function(name=r_func_name, input_key=r_executed["inputKey"],
                    outputs=Outputs(r_executed["outputs"]),
                    body=test_clustering.get_body(r_executed), source=r_source_file)
  pd_func = Function(name=pd_func_name, input_key=pd_executed["inputKey"],
                     outputs=Outputs(pd_executed["outputs"]),
                     body=test_clustering.get_body(pd_executed), source=pd_source_file)
  print(test_clustering.execution_similarity(r_func, pd_func))


def delta(r_func_name, pd_func_name):
  r_func = r_functions.get_r_function(r_source_file, r_func_name)
  pd_func = pd_functions.get_pd_functions(pd_source_file, as_dict=True)[pd_func_name]
  generated_args = get_generated_args(r_func, 1)
  print(generated_args[0])
  r_result = r_functions.execute_R_function_on_args(r_func, generated_args)[0]
  pd_result = pd_functions.execute_pd_function_on_args(pd_func, generated_args)[0]
  difference = dataframer.difference(r_result['return'], pd_result['return'])
  print(difference)


if __name__ == "__main__":
  # compare_functions("gen_func_r_select3", "func_py_select1")
  delta("gen_func_r_select3", "func_py_select1")
  # delta("gen_func_r_head", "func_py_head")
