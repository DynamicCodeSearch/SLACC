from __future__ import print_function, division
import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


from readers.python_parser import commented_functions_in_folder
from utils import lib


def _commented_functions():
  folder = "data/pyfiles_dump/functions"
  write_folder = "data/pyfiles_dump/commented_functions"
  size = None
  n_jobs = 1
  args = sys.argv
  if len(args) >= 2 and lib.is_int(args[1]):
    n_jobs = int(args[1])
  commented_functions_in_folder(folder, write_folder, size, n_jobs)


def _commented_functions_mini():
  folder = "data/pyfiles_dump/functions"
  write_folder = "data/pyfiles_dump/commented_functions_mini"
  size = 1000
  n_jobs = 1
  args = sys.argv
  if len(args) >= 2 and lib.is_int(args[1]):
    n_jobs = int(args[1])
  commented_functions_in_folder(folder, write_folder, size, n_jobs)


if __name__ == "__main__":
  _commented_functions_mini()
  _commented_functions()
