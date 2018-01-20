from __future__ import print_function, division
import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from readers.python_parser import aggregate


def _aggregate():
  folder = "data/pyfiles_dump/stats/indeps"
  destination_path = "data/pyfiles_dump/stats/all.pkl"
  aggregate(folder, destination_path)


if __name__ == "__main__":
  _aggregate()
