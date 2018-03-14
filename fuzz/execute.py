from __future__ import print_function, division
import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import ctypes
from optparse import OptionParser
import re
from utils import cache
import signal

SPLIT_PATTERN = ''',(?=(?:[^'"]|'[^']*'|"[^"]*")*$)'''


def timeout_handler(signum, frame):  # Custom signal handler
  raise Exception("Function timed out.")

# Change the behavior of SIGALRM
signal.signal(signal.SIGALRM, timeout_handler)


def split(line):
  return re.split(SPLIT_PATTERN, line)


def get_opt_args():
  parser = OptionParser(usage='usage: python fuzz/ a%prog [options] arguments')
  parser.add_option('-s', '--source',
                    dest='source', help="Location of source executable file")
  parser.add_option('-f', '--function',
                    dest='function', help="Name of function to be executed")
  parser.add_option('-t', '--argTypes',
                    dest='arg_types', help="Types of arguments separated by comma(',')")
  parser.add_option('-v', '--argVals',
                    dest='arg_vals', help="Values of arguments separated by comma(',')")
  parser.add_option('-r', '--retType',
                    dest='ret_type', help="Type of return(',')")
  (options, args) = parser.parse_args()
  if not options.source:
    parser.error("Location of source file name not given")
  if not options.function:
    parser.error("Name of function")
  if not options.arg_types:
    parser.error("Types of arguments not provided")
  if not options.arg_vals:
    parser.error("Values of arguments not provided")
  if not options.ret_type:
    parser.error("Return type of function not provided")
  return options, args


def get_c_arg(data_type):
  if data_type == "int":
    return ctypes.c_int
  elif data_type == "float":
    return ctypes.c_float
  elif data_type == "char":
    return ctypes.c_char


def escaped_str(ch):
  if len(ch) <= 1:
    return ch
  else:
    return ch[1:-1]


def get_py_arg(data_type):
  if data_type == "int":
    return int
  elif data_type == "float":
    return float
  elif data_type == "char":
    return escaped_str


def process_arg_types(arg_types):
  c_arg_types, py_arg_types = [], []
  for arg_type in split(arg_types):
    c_arg_types.append(get_c_arg(arg_type))
    py_arg_types.append(get_py_arg(arg_type))
  return c_arg_types, py_arg_types


def cast_vals(arg_vals, py_arg_types, c_arg_types):
  return [c_arg_type(py_arg_type(arg_val)) for c_arg_type, py_arg_type, arg_val in zip(c_arg_types, py_arg_types, split(arg_vals))]


def execute_c(source_exec, function_name, arg_types, arg_vals, ret_type):
  prefix = source_exec.rsplit(".", 1)[0]
  module = ctypes.cdll.LoadLibrary(source_exec)
  signal.alarm(2)
  try:
    c_function = module[function_name]
  except AttributeError:
    print("Static Exception")
    raise Exception("Not found. Probably static method")
  c_arg_types, py_arg_types = process_arg_types(arg_types)
  c_function.argtypes = c_arg_types
  c_function.restype = get_c_arg(ret_type)
  c_arg_vals = cast_vals(arg_vals, py_arg_types, c_arg_types)
  ret_val = c_function(*c_arg_vals)
  res_file = "%s.pkl" % prefix
  cache.save(res_file, ret_val)


def main():
  (options, args) = get_opt_args()
  execute_c(options.source, options.function, options.arg_types, options.arg_vals, options.ret_type)


if __name__ == "__main__":
  main()
