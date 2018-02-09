from __future__ import print_function, division
import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from pycparser import parse_file
from pycparser.plyparser import ParseError
from utils import cache
import signal

FAKE_LIBS_PATH = "utils/fake_libc_include"
AST_SAVE = "temp/ast.pkl"


class TimeoutException(Exception):  # Custom exception class
  pass


def timeout_handler(signum, frame):  # Custom signal handler
  raise TimeoutException

# Change the behavior of SIGALRM
signal.signal(signal.SIGALRM, timeout_handler)


def parse(path):
  signal.alarm(5)
  ast = parse_file(path, use_cpp=True, cpp_args=[r'-I%s' % FAKE_LIBS_PATH])
  cache.save(AST_SAVE, ast)


if __name__ == "__main__":
  args = sys.argv
  if len(args) == 2:
    parse(args[1])
