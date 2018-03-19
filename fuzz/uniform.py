from __future__ import print_function, division
import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from utils import cache, lib
from c_utils.c_parser import Function, Arg, Return
import ctypes
from utils.logger import get_logger
import logging
import signal
if os.name == 'posix' and sys.version_info[0] < 3:
  import subprocess32 as subprocess
else:
  import subprocess
from joblib import Parallel, delayed
from multiprocessing import Pool
import argparse


LOG_LEVEL = logging.INFO
logger = get_logger(__name__, LOG_LEVEL)


def get_file_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("-n", "--n_jobs", type=int, default=2, help="Number of jobs")
  parser.add_argument("-f", "--function", type=str, default="oops", help="Fuzz functions")
  return parser.parse_args()


def load_c_functions(file_name):
  return cache.load(file_name)


def save_source(source_name, source, is_static):
  prefix = source_name.split(".c")[0]
  file_source = source.replace("static ", "") if is_static else source
  source_file = cache.create_file_path("temp", source_name)
  with open(source_file, 'wb') as f:
    f.write(file_source)
  status = os.system("gcc -fPIC -shared -o temp/%s.so temp/%s > /dev/null 2>&1" % (prefix, source_name))
  return "temp/%s.so" % prefix, status


def get_c_arg(data_type):
  if data_type == "int":
    return ctypes.c_int
  elif data_type == "float":
    return ctypes.c_float
  elif data_type == "char":
    return ctypes.c_char


def exec_function(source_exec, function_name, arg_types, arg_vals, ret_type, timeout=5):
  cmd = ["python", "fuzz/execute.py", "-s", source_exec, "-f", function_name, "-t", arg_types,
         '-v', arg_vals, '-r', ret_type]
  ret_data, error = None, None
  proc = subprocess.Popen(cmd, stderr=subprocess.PIPE)
  try:
    out, err, = proc.communicate(timeout=timeout)
  except subprocess.TimeoutExpired:
    error = "Timed out after %d seconds" % timeout
    return ret_data, error
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
  source_exec, status = save_source(function.source_name, function.source, function.is_static)
  if status != 0:
    error = "Failed to compile: %s" % function.source_name
    cache.delete("temp/%s" % function.source_name)
    cache.delete(source_exec)
    return None, error
  c_arg_types = ",".join([arg.type for arg in function.args])
  fuzzable_args = function.get_fuzzable_args()
  rets = []
  c_ret_type = function.ret.type
  for fuzzable_arg in fuzzable_args:
    c_arg_vals = ",".join(map(str, fuzzable_arg))
    ret, error = exec_function(source_exec, function.name, c_arg_types, c_arg_vals, c_ret_type)
    rets.append((fuzzable_arg, ret, error))
  cache.delete("temp/%s" % function.source_name)
  cache.delete(source_exec)
  return rets, None


def fuzz_functions(functions_file, save_folder, arg_limit=None):
  prefix = functions_file.rsplit("/", 1)[-1].split(".")[0]
  logger.info("Running for %s.pkl" % prefix)
  temp_file = cache.create_file_path(save_folder, prefix, ext=".tmp")
  save_file = cache.create_file_path(save_folder, prefix, ext=".pkl")
  if cache.file_exists(save_file):
    logger.info("%s file exists" % save_file)
    return
  if cache.file_exists(temp_file):
    logger.info("%s file being processed" % save_file)
    return
  cache.save(temp_file, {"Processing": True})
  functions = load_c_functions(functions_file)
  cnt, fuzzables = 0, 0
  results = {}
  n_functions = len(functions)
  for function in functions:
    cnt += 1
    if function.is_fuzzable(arg_limit=arg_limit):
      fuzzables += 1
      fuzzed, error = fuzz(function)
      results[cnt] = {
          "results": fuzzed,
          "error": error,
          "function": function
      }
    if cnt % 25 == 0:
      logger.info("In %s.pkl; Fuzzed %d/%d of functions. Fuzzed funcs: %d" % (prefix, cnt, n_functions, fuzzables))
  logger.info("Finished %s.pkl; Fuzzed funcs: %d/%d" % (prefix, fuzzables, n_functions))
  cache.delete(temp_file)
  cache.save(save_file, results)


def wrap_fuzz_functions(args):
  fuzz_functions(*args)


def fuzz_functions_folder(source_folder, destination_folder, n_jobs, arg_limit):
  files = []
  for source_file in cache.list_files(source_folder, is_relative=False):
    extension = source_file.rsplit(".", 1)[-1]
    prefix = source_file.rsplit("/", 1)[-1].split(".")[0]
    destination_file = cache.create_file_path(destination_folder, prefix, ".pkl")
    if extension == "pkl" and not cache.file_exists(destination_file):
      files.append(source_file)

  try:
    p = Pool(processes=n_jobs)
    args = [(source_file, destination_folder, arg_limit) for source_file in files]
    p.map(wrap_fuzz_functions, args)
    # Parallel(n_jobs=n_jobs)(
    #     delayed(fuzz_functions)(source_file, destination_folder, arg_limit) for source_file in files)
  except (KeyboardInterrupt, IOError) as e:
    logger.info("** ERROR WHILE PARALLEL PROCESSING. RESTARTING ALL OVER AGAIN")
    for temp_file in cache.list_files(destination_folder, is_relative=False):
      extension = temp_file.rsplit(".", 1)[-1]
      if extension == "tmp":
        cache.delete(temp_file)
    fuzz_functions_folder(source_folder, destination_folder, n_jobs, arg_limit)


def aggregate(source_folder, destination_file):
  """
  Aggregate all files in folder and dump in destination
  :param source_folder:
  :param destination_file:
  :return:
  """
  cnt = 0
  aggregated = {}
  for source_file in cache.list_files(source_folder, is_relative=False):
    extension = source_file.rsplit(".", 1)[-1]
    if extension != "pkl": continue
    logger.info("Processing %s" % source_file)
    source = cache.load(source_file)
    if source:
      functions = cache.load(source_file).values()
      for function in functions:
        aggregated[cnt] = function
        cnt += 1
  logger.info("Total number of functions = %d" % cnt)
  cache.save(destination_file, aggregated)


def _aggregate():
  source_folder = "data/cfiles_dump/valids_all/uniform_fuzzed"
  destination_file = "data/cfiles_dump/valids_all/uniform_aggregate.pkl"
  aggregate(source_folder, destination_file)


def _fuzz_functions_folder(args):
  source_folder = "data/cfiles_dump/valids_all/functions"
  destination_folder = "data/cfiles_dump/valids_all/uniform_fuzzed"
  arg_limit = 4
  n_jobs = args.n_jobs
  logger.info("RUNNING %d JOBS" % n_jobs)
  fuzz_functions_folder(source_folder, destination_folder, n_jobs, arg_limit)


def _test_ctypes():
  # import ctypes
  _module = ctypes.CDLL("temp/add.so")
  _module['add'].argtypes = (ctypes.c_int, ctypes.c_int)
  result = _module['add'](ctypes.c_int(5), ctypes.c_int(6))
  print(result)
  return int(result)


def _test_remote_call():
  # cmd = ["python", "fuzz/execute.py", "-s", "temp/val-prof-7.so", "-f", "foo", "-t", 'int', '-v', '-5']
  # cmd = ["python", "fuzz/execute.py", "-s", "temp/fibo2.so", "-f", "fib2", "-t", 'int', '-v', '100']
  os.system("gcc -fPIC -shared -o temp/gofast.so temp/gofast.c > /dev/null 2>&1")
  cmd = ["python", "fuzz/execute.py", "-s", "temp/gofast.so", "-f", "stupid", "-t",
         'int,int', '-v', '16396,16396', '-r', 'int']
  proc = subprocess.Popen(cmd, stderr=subprocess.PIPE)
  out, err, = proc.communicate(timeout=5)
  print(out)
  print(err)
  print(cache.load('temp/gofast.pkl'))
  print(proc.returncode, -signal.SIGSEGV)


def _verify():
  data = cache.load("data/cfiles_dump/fuzzed/uniform.pkl")
  n_fuzzed = len(data)
  failed = 0
  for val in data.values():
    if len(val["results"]) == 0:
      failed += 1
  print(failed, n_fuzzed)


def _main():
  args = get_file_args()
  f_name = args.function
  if f_name == "fuzz":
    _fuzz_functions_folder(args)
  elif f_name == "aggregate":
    _aggregate()
  else:
    print("WTF is %s!!!" % f_name)


if __name__ == "__main__":
  # _test()
  # _test_remote_call()
  # _verify()
  _main()
