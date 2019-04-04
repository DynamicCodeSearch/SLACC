import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


from sos.rUtils import functions


def process_file(file_path):
  r_functions = functions.get_r_functions(file_path)
  n_valid = 0
  print("Processing %d functions from '%s' ... " % (len(r_functions), file_path))
  for func_name, r_func in r_functions.items():
    # print(type(r_func.formals()))
    evaluated = functions.process_R_function(file_path, func_name, r_func)
    if evaluated is not None and "outputs" in evaluated:
      n_valid += 1
      functions.save_function(evaluated)
  print("Valid functions: %d/%d" % (n_valid, len(r_functions)))


if __name__ == "__main__":
  process_file('/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/R/Example/PandasR/r_snippets.R')
  # _test_extract_col_names()
