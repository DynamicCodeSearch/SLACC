import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

from rpy2.robjects.vectors import DataFrame, FloatVector, IntVector, StrVector, ListVector, FactorVector
import numpy
from collections import OrderedDict

__author__ = "bigfatnoob"


def is_bracket_balanced(expression):
  """
  Finds out how balanced an expression is.
  With a string containing only brackets.

  >> is_matched('[]()()(((([])))')
  False
  >> is_matched('[](){{{[]}}}')
  True
  """
  opening = tuple('({[')
  closing = tuple(')}]')
  mapping = dict(zip(opening, closing))
  queue = []
  for letter in expression:
    if letter in opening:
      queue.append(mapping[letter])
    elif letter in closing:
      if not queue or letter != queue.pop():
        return False
  return not queue


def convert_r_list_to_py(r_list):
  r_dict_types = [DataFrame, ListVector]
  r_array_types = [FloatVector, IntVector]
  r_list_types = [StrVector, FactorVector]
  if type(r_list) in r_dict_types:
    keys = r_list.names
    if not keys:
      keys = range(0, len(r_list))
    return OrderedDict(zip(keys, [convert_r_list_to_py(elt) for elt in r_list]))
  elif type(r_list) in r_list_types:
    return [convert_r_list_to_py(elt) for elt in r_list]
  elif type(r_list) in r_array_types:
    return numpy.array(r_list)
  else:
    if hasattr(r_list, "rclass"): # An unsupported r class
      print(r_list)
      exit()
      raise KeyError('Could not proceed, type {} is not defined'.format(type(r_list)))
    else:
      return r_list # We reached the end of recursion