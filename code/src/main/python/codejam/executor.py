import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from analysis import execute
import properties


def execute_problem(problem_id):
  execute.execute_problem(properties.CODE_JAM, problem_id)


if __name__ == "__main__":
  args = sys.argv
  if len(args) < 2:
    print("Use python codejam/file_meta_data.py <problem_id>")
    exit(0)
  execute_problem(args[1])
