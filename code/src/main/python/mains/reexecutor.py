import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from analysis import execute


def reexecute(dataset):
  execute.reexecute_functions(dataset)


if __name__ == "__main__":
  args = sys.argv
  if len(args) < 2:
    print("Use python codejam/file_meta_data.py <problem_id>")
    exit(0)
  else:
    reexecute(args[1])
