import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


from misconceptions.pdUtils import functions


def process_file(file_path):
  pd_functions = functions.get_pd_functions(file_path)
  n_valid = 0
  print("Processing %d functions from '%s' ... " % (len(pd_functions), file_path))
  for pd_func in pd_functions:
    evaluated = functions.process_pd_function(file_path, pd_func)
    if evaluated is not None and "outputs" in evaluated:
      n_valid += 1
      functions.save_function(evaluated)
  print("Valid functions: %d/%d" % (n_valid, len(pd_functions)))


def _test_extract_col_names():
  file_name = "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/python/Example/PandasR/generated_py_dxyz.py"
  func_name = "func_py_select2"
  print(functions.parse_function_for_col_names(func_name, file_name))


if __name__ == "__main__":
  process_file("/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/python/Example/PandasR/generated_py_d123.py")
  # _test_extract_col_names()
