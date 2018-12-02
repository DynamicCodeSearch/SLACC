import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


from analysis import execute
import properties


def reexecute():
  execute.reexecute_functions(properties.CODE_JAM)


if __name__ == "__main__":
  reexecute()
