import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from utils.lib import O


ROOT_SCOPE = "__ROOT__"

VAR_TYPE = O(
  GLOBAL="global",
  LOCAL="local",
  ARG="arg",
  VARARG="vararg",
  KWARG="kwarg"
)

SCOPE_SEPARATOR = "->"

PRIMITIVES = {'int', 'long', 'float', 'str', 'bool'}

GENERATED_PREFIX = "generated_py_"

TEMPORARY_PREFIX = "tmp_py_"

FUNCTION_PREFIX = "func_"

# In seconds
METHOD_WAIT_TIMEOUT = 1