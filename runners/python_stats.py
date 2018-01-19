from __future__ import print_function, division
import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from readers.python_parser import collect_stats_for_all
from utils import lib


def _collect_statistics():
  folder = "data/pyfiles_dump/functions"
  destination_path = "data/pyfiles_dump/stats/"
  n_jobs = 1
  args = sys.argv
  if len(args) >= 2 and lib.is_int(args[1]):
    n_jobs = int(args[1])
  collect_stats_for_all(folder, destination_path, n_jobs)


if __name__ == "__main__":
  _collect_statistics()
