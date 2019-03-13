import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from analysis import execute


def execute_dataset(dataset):
  execute.execute_problem(dataset)


def execute_problem(dataset, problem_id):
  execute.execute_problem(dataset, problem_id)


if __name__ == "__main__":
  args = sys.argv
  if len(args) < 2:
    print("Use python mains/executor.py <problem_id>")
    exit(0)
  elif len(args) > 2:
    execute_problem(args[1], args[2])
  else:
    execute_dataset(args[1])
