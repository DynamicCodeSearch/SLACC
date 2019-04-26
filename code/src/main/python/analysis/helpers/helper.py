import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


import ast
import inspect
import re
import uuid

from analysis.helpers import constants as a_consts
from utils import cache
import properties


LIST_KEY_PATTERN = re.compile('(\(.+\))@(\d+)')


def get_type(val):
  return type(val).__name__


def generate_random_string():
  return str(uuid.uuid4()).replace("-", "")


def compile_py(file_name):
  source = cache.read_file(file_name)
  ast.parse(source)
  # compile(source, file_name, 'exec')


def import_file(file_path, src_home=properties.PYTHON_PROJECTS_HOME):
  python_name = file_path.split(src_home)[-1][1:].split(".")[0].replace(os.path.sep, ".")
  module = __import__(python_name)
  parts = python_name.split(".")
  for part in parts[1:]:
    module = getattr(module, part)
  return module


def is_valid_file(file_path, src_home=properties.PYTHON_PROJECTS_HOME):
  try:
    import_file(file_path, src_home)
    return True
  except Exception:
    return False


def get_generated_functions(file_path, as_dict=False):
  sys.path.append(properties.PYTHON_PROJECTS_HOME)
  module = import_file(file_path)
  sys.path.remove(properties.PYTHON_PROJECTS_HOME)
  functions = {}
  for name in dir(module):
    if name.startswith(a_consts.FUNCTION_PREFIX):
      functions[name] = getattr(module, name)
  if not as_dict:
    return functions.values()
  return functions


def get_function(file_path, function_name, src_home=properties.PYTHON_PROJECTS_HOME):
  sys.path.append(src_home)
  module = import_file(file_path, src_home)
  sys.path.remove(src_home)
  return getattr(module, function_name, None)


def get_func_arg_names(func):
  return inspect.getargspec(func).args


def get_func_body(func):
  return inspect.getsource(func)


def get_family_name(type_name):
  if type_name == "int":
    return "int"
  elif type_name == "long":
    return "int"
  elif type_name == "str":
    return "string"
  elif type_name == "float":
    return "float"
  elif type_name == "bool":
    return "boolean"
  else:
    return None


def is_list_key(key):
  return LIST_KEY_PATTERN.match(key) is not None


def parse_list_key(key):
  matches = LIST_KEY_PATTERN.match(key)
  if not matches:
    return None, None
  return matches.group(1), int(matches.group(2))


def get_simple_name(file_name):
  return file_name.split(properties.PYTHON_PROJECTS_HOME)[-1][1:]


def generate_function_name():
  return "%s%s" % (a_consts.FUNCTION_PREFIX, generate_random_string())


def generate_py_file_name():
  return "%s%s" % (a_consts.GENERATED_PREFIX, generate_random_string())


def generate_py_temp_name():
  return "%s%s" % (a_consts.TEMPORARY_PREFIX, generate_random_string())


if __name__ == "__main__":
  get_generated_functions("/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/python/Y11R5P1/dozingcat/generated_py_15cf7f9f3c2c48ccab3c0a8dc3ce4884.py")
  # compile_py("/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/python/stupid/temp_asewqeqwewqe.py")