from __future__ import print_function, division
import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from utils import cache
from c_utils.c_parser import Function, Arg, Return
import ctypes
from utils.logger import get_logger
import logging


LOG_LEVEL = logging.INFO
logger = get_logger(__name__, LOG_LEVEL)

VALID_FILE = "data/cfiles_dump/valids/functions.pkl"


def load_c_functions(file_name=VALID_FILE):
  return cache.load(file_name)


def save_source(source_name, source):
  prefix = source_name.split(".c")[0]
  with open("temp/%s" % source_name, 'wb') as f:
    f.write(source)
  status = os.system("gcc -fPIC -shared -o temp/%s.so temp/%s > /dev/null 2>&1" % (prefix, source_name))
  print(status)
  assert status == 0
  cache.delete("temp/%s" % source_name)
  return "temp/%s.so" % prefix


def get_c_arg(data_type):
  if data_type == "int":
    return ctypes.c_int
  elif data_type == "float":
    return ctypes.c_float
  elif data_type == "char":
    return ctypes.c_char


def exec_function(c_function, arg_types, arg_vals):
  args = [a_type(a_val) for a_type, a_val in zip(arg_types, arg_vals)]
  return c_function(*args)


def fuzz(function):
  source_exec = save_source(function.source_name, function.source)
  module = ctypes.CDLL(source_exec)
  c_arg_types = [get_c_arg(arg.type) for arg in function.args]
  c_function = module[function.name]
  c_function.argtypes = tuple(c_arg_types)
  fuzzable_args = function.get_fuzzable_args()
  rets = []
  for fuzzable_arg in fuzzable_args:
    rets.append(exec_function(c_function, c_arg_types, fuzzable_arg))
  cache.delete(source_exec)
  return rets


def _main():
  functions = load_c_functions()
  cnt = 0
  for function in functions:
    if function.is_fuzzable():
      # print(function.get_fuzzable_args())
      fuzz(function)
      # exit()


def _test():
  # import ctypes
  _module = ctypes.CDLL("temp/add.so")
  _module['add'].argtypes = (ctypes.c_int, ctypes.c_int)
  result = _module['add'](ctypes.c_int(5), ctypes.c_int(6))
  print(result)
  return int(result)



if __name__ == "__main__":
  _main()
  # _test()