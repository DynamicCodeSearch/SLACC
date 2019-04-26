import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import numpy as np
import pandas as pd

from utils.lib import O2
from rpy2.robjects import pandas2ri


pandas2ri.activate()


class DataFrame(O2):
  def __init__(self):
    self.name = None
    self.columns = None
    O2.__init__(self)

  def has_column(self, col_name):
    return self.columns and col_name in self.columns


class Series(O2):
  def __init__(self):
    self.name = None
    self.type = None
    self.levels = None
    self.values = None
    self.min = None
    self.max = None
    self.has_NAN = False
    O2.__init__(self)


def convert_py_object_to_r(py_obj):
  if type(py_obj) == pd.core.frame.DataFrame:
    return pandas2ri.py2ri(py_obj)
  raise RuntimeError("Currently does not support type: %s" % type(py_obj))


def convert_r_object_to_py(r_obj):
  return pandas2ri.ri2py(r_obj)


def is_dataframe_type(data_type):
  name = data_type.__name__
  return name.endswith("DataFrame")


def analyze_sample_variable(var):
  if is_dataframe_type(type(var)):
    return analyze_sample_dataframe(var)
  raise RuntimeError("Sorry. Supports only data frames!")


def analyze_sample_dataframe(sample_df):
  df = DataFrame()
  col_names = {}
  for name in sample_df.colnames:
    column = analyze_series(sample_df.rx2(name))
    column.name = name
    col_names[name] = column
  df.columns = col_names
  return df


def analyze_series(series):
  column = Series()
  if series.rclass[0] == "logical":
    column.type = bool
  elif series.rclass[0] == "factor":
    column.type = str
    column.levels = convert_r_object_to_py(series.levels)
  elif series.rclass[0] == "numeric":
    is_int = True
    for val in convert_r_object_to_py(series):
      if not np.isnan(val) and val != int(val):
        is_int = False
    column.type = int if is_int else float
  return column
