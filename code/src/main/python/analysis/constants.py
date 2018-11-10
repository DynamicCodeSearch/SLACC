import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from utils.lib import O


ROOT_SCOPE = "$ROOT$"

VAR_TYPE = O(
  GLOBAL="global",
  LOCAL="local",
  ARG="arg",
  VARARG="vararg",
  KWARG="kwarg"
)

SCOPE_SEPARATOR = "->"

PRIMITIVES = {'int', 'long', 'float', 'str'}


