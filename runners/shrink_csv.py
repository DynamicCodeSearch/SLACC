from __future__ import print_function, division
import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from readers.python_parser import shrink_csv_files_in_folder
from utils import lib


def _shrink_csv():
  folder = "data/pyfiles_dump/csv"
  write_folder = "data/pyfiles_dump/csv_mini"
  size = 100
  n_jobs = 1
  args = sys.argv
  if len(args) >= 2 and lib.is_int(args[1]):
    n_jobs = int(args[1])
  shrink_csv_files_in_folder(folder, write_folder, size, n_jobs)


if __name__ == "__main__":
  _shrink_csv()
