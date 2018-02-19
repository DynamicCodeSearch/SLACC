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
import subprocess
import signal


LOG_LEVEL = logging.INFO
logger = get_logger(__name__, LOG_LEVEL)

VALID_FILE = "data/cfiles_dump/valids/functions.pkl"


def load_c_functions(file_name=VALID_FILE):
  return cache.load(file_name)


def save_source(source_name, source):
  prefix = source_name.split(".c")[0]
  source_file = cache.create_file_path("temp", source_name)
  with open(source_file, 'wb') as f:
    f.write(source)
  status = os.system("gcc -fPIC -shared -o temp/%s.so temp/%s > /dev/null 2>&1" % (prefix, source_name))
  return "temp/%s.so" % prefix, status


def get_c_arg(data_type):
  if data_type == "int":
    return ctypes.c_int
  elif data_type == "float":
    return ctypes.c_float
  elif data_type == "char":
    return ctypes.c_char


def exec_function(source_exec, function_name, arg_types, arg_vals):
  cmd = ["python", "fuzz/execute.py", "-s", source_exec, "-f", function_name, "-t", arg_types, '-v', arg_vals]
  ret_data, error = None, None
  proc = subprocess.Popen(cmd, stderr=subprocess.PIPE)
  out, err, = proc.communicate()
  if proc.returncode == -signal.SIGSEGV:
    error = "Segmentation Fault"
    return ret_data, error
  prefix = source_exec.rsplit(".", 1)[0]
  res_file = "%s.pkl" % prefix
  if cache.file_exists(res_file):
    ret_data = cache.load(res_file)
    cache.delete(res_file)
  else:
    error = err
  return ret_data, error


def fuzz(function):
  source_exec, status = save_source(function.source_name, function.source)
  if status != 0:
    print("Failed to compile: %s" % function.source_name)
    cache.delete("temp/%s" % function.source_name)
    cache.delete(source_exec)
    return None
  c_arg_types = ",".join([arg.type for arg in function.args])
  fuzzable_args = function.get_fuzzable_args()
  rets = []
  for fuzzable_arg in fuzzable_args:
    c_arg_vals = ",".join(map(str, fuzzable_arg))
    ret, error = exec_function(source_exec, function.name, c_arg_types, c_arg_vals)
    rets.append((fuzzable_arg, ret, error))
  cache.delete("temp/%s" % function.source_name)
  cache.delete(source_exec)
  return rets


def _main():
  functions = load_c_functions()
  cnt = 0
  for function in functions:
    if function.is_fuzzable():
      cnt += 1
      print(function.name)
      fuzzed = fuzz(function)
      print(fuzzed)
      if cnt == 10: break
      # exit()


def _test_ctypes():
  # import ctypes
  _module = ctypes.CDLL("temp/add.so")
  _module['add'].argtypes = (ctypes.c_int, ctypes.c_int)
  result = _module['add'](ctypes.c_int(5), ctypes.c_int(6))
  print(result)
  return int(result)


def _test_remote_call():
  # cmd = ["python", "fuzz/execute.py", "-s", "temp/val-prof-7.so", "-f", "foo", "-t", 'int', '-v', '-5']
  cmd = ["python", "fuzz/execute.py", "-s", "temp/piggyback.so", "-f", "align", "-t", 'int', '-v', '15']
  proc = subprocess.Popen(cmd, stderr=subprocess.PIPE)
  out, err, = proc.communicate()
  print(out)
  print(err)
  print(proc.returncode, -signal.SIGSEGV)




if __name__ == "__main__":
  _main()
  # _test()
  # _test_remote_call()