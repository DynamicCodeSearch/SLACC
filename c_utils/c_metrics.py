from __future__ import print_function, division
import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


from utils.lib import O
from utils import cache
from c_utils.c_parser import Function, Arg, Return
from utils.logger import get_logger
import logging
import re

LOG_LEVEL = logging.INFO
logger = get_logger(__name__, LOG_LEVEL)

FUZZABLE = {"int", "float", "char"}
PRINT_F = re.compile(r'printf\(')
SCAN_F = re.compile(r'scanf\(')


def is_valid_arg(arg):
  return (not arg.is_enum) and (not arg.is_func) and (not arg.is_ptr) and \
         (not arg.is_struct) and (not arg.is_union) and (not arg.is_arr) and \
         (arg.type in FUZZABLE)


def is_valid_ret(ret):
  return (not ret.is_enum) and (not ret.is_ptr) and (not ret.is_struct) and \
         (not ret.is_union) and (ret.type in FUZZABLE)

def check_func_io(body):
  return PRINT_F.search(body) is not None, SCAN_F.search(body) is not None


class Metrics(O):
  def __init__(self):
    O.__init__(self)
    self.n_args = {}
    self.n_valid_args = {}
    self.stds = {
             "reads": 0,
             "writes": 0,
             "reads_writes": 0,
             "n_reads_writes": 0
           }
    self.mains = 0
    self.rets = 0
    self.valid_rets = 0
    self.n_functions = 0


def compute_metrics(file_name, save_file):
  metrics = Metrics()
  functions = cache.load(file_name, verbose=False)
  n_functions = len(functions)
  metrics.n_functions = n_functions
  for i, func in enumerate(functions):
    if func.name == "main":
      metrics.mains += 1
      continue
    n_func_args = len(func.args)
    metrics.n_args[n_func_args] = metrics.n_args.get(n_func_args, 0) + 1
    is_fuzzable_args = n_func_args > 0
    for arg in func.args:
      if not is_valid_arg(arg):
        is_fuzzable_args = False
        break
    if is_fuzzable_args:
      metrics.n_valid_args[n_func_args] = metrics.n_valid_args.get(n_func_args, 0) + 1
    if func.ret:
      metrics.rets += 1
      if is_valid_ret(func.ret):
        metrics.valid_rets += 1
    contains_print, contains_scan = check_func_io(func.body)
    if contains_print and contains_scan:
      metrics.stds['reads_writes'] += 1
    elif contains_print:
      metrics.stds['writes'] += 1
    elif contains_scan:
      metrics.stds['reads'] += 1
    else:
      metrics.stds['n_reads_writes'] += 1
    if (i + 1) % 100 == 0:
      logger.info("Processed %d/%d of functions." % (i + 1, n_functions))
  logger.info("Processed all. Check %s" % save_file)
  cache.save(save_file, metrics)
  print(metrics)


def _metrics():
  compute_metrics("data/cfiles_dump/valids/functions.pkl", "data/cfiles_dump/valids/function_metrics.pkl")


if __name__ == "__main__":
  _metrics()
