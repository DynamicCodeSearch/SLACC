import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


import uuid
import ast
from utils import cache
import properties


def get_type(val):
  return type(val).__name__


def generate_random_string():
  return str(uuid.uuid4()).replace("-", "")


def compile_py(file_name):
  source = cache.read_file(file_name)
  ast.parse(source)
  # compile(source, file_name, 'exec')


def import_file(file_path):
  python_name = file_path.split(properties.PYTHON_PROJECTS_HOME)[-1][1:].split(".")[0].replace(os.path.sep, ".")
  module = __import__(python_name)
  parts = python_name.split(".")
  for part in parts[1:]:
    module = getattr(module, part)
  return module


if __name__ == "__main__":
  mod = import_file("/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/python/Y11R5P1/dennislissov/A.py")
  print(dir(mod))
  # compile_py("/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/python/stupid/temp_asewqeqwewqe.py")