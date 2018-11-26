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


def is_valid_file(file_path):
  try:
    import_file(file_path)
    return True
  except Exception:
    return False


def get_generated_functions(file_path):
  sys.path.append(properties.PYTHON_PROJECTS_HOME)
  module = import_file(file_path)
  sys.path.remove(properties.PYTHON_PROJECTS_HOME)
  print(dir(module))


if __name__ == "__main__":
  get_generated_functions("/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/python/Y11R5P1/dennislissov/generated_py_894b4b91802947cabb56ff23de4cf62f.py")
  # compile_py("/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/python/stupid/temp_asewqeqwewqe.py")