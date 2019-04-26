import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


import pandas as pd
import numpy as np
import re

from misconceptions.common import datatypes
from misconceptions.common.differences import DataFrameDiffMeta


def extract_col_names(arg_name, func_body):
  COL_NAME_REGEX1 = '(?:[a-zA-Z][a-zA-Z0-9_.]*)|(?:[.][^0-9][a-zA-Z0-9_.]+)'
  # Example df$Group + df$.1Group + df$._WTF'
  arg_regex1 = r'%s(?:\[.+\])?\$(%s)' % (arg_name, COL_NAME_REGEX1)
  # Example df[, c("col1", "col2")]
  COL_NAME_REGEX2 = r"[\'\"](%s)[\'\"]" % COL_NAME_REGEX1
  arg_regex2 = r'%s\[.*?\,\s*c\(\s*%s(?:\s*?,\s*?%s)*\)\]' % (arg_name, COL_NAME_REGEX2, COL_NAME_REGEX2)
  # Example df[["col1", "col2"]]
  arg_regex3 = r'%s\[\[\s*%s(?:\s*?,\s*?%s)*\]\]' % (arg_name, COL_NAME_REGEX2, COL_NAME_REGEX2)
  # Example select(df, A:E)
  arg_regex4 = r'(?:%s)\(%s\s*,\s*(%s)(?:\s*?:\s*?(%s))?' % (COL_NAME_REGEX1, arg_name, COL_NAME_REGEX1, COL_NAME_REGEX1)
  # Example select(df, A:E)
  arg_regex5 = r'(?:%s)\(%s\s*,\s*%s(?:\s*?:\s*?%s)?' % (COL_NAME_REGEX1, arg_name, COL_NAME_REGEX2, COL_NAME_REGEX2)
  # Example select(df, 'A':'E')
  matches1 = re.findall(arg_regex1, func_body)
  matches2 = re.findall(arg_regex2, func_body)
  matches3 = re.findall(arg_regex3, func_body)
  matches4 = re.findall(arg_regex4, func_body)
  matches5 = re.findall(arg_regex5, func_body)
  col_names = set()
  for match in matches1:
    if match and match.strip():
      col_names.add(match)
  for match in matches2 + matches3 + matches4 + matches5:
    for col_name in list(match):
      if col_name and col_name.strip():
        col_names.add(col_name)
  if col_names:
    df = datatypes.DataFrame()
    df.name = arg_name
    df.columns = {}
    for name in sorted(list(col_names)):
      column = datatypes.Series()
      column.name = name
      df.columns[name] = column
    return df
  return None

def test_col_diff():
  print("Col Diff")
  df1 = pd.DataFrame(np.array([[1,2,3], [4,5,6], [7,8,9]]), columns=["a", "b", "c"])
  df2 = pd.DataFrame(np.array([[5, 1,2,3], [3, 4,5,6], [7, 7,8,9]]), columns=["x","a", "b", "c"])
  print(DataFrameDiffMeta.col_diff(df1, df2))


def test_row_diff():
  print("Row Diff")
  df1 = pd.DataFrame(np.array([[1,2,3], [4,5,6], [7,8,9]]), columns=["a", "b", "c"])
  df2 = pd.DataFrame(np.array([[0,-1,-3], [1,2,3], [4,5,6], [7,8,9], [0,-1,-3]]), columns=["a", "b", "c"])
  print(DataFrameDiffMeta.row_diff(df1, df2))


def test_double_diff_1():
  print("Double Diff - 1")
  df1 = pd.DataFrame(np.array([[1,2,3,4], [4,5,6,7]]), columns=["a", "b", "c", "d"])
  df2 = pd.DataFrame(np.array([[3,4], [1,2], [4,5], [9,7], [3, 3]]), columns=["a", "b"])
  print(DataFrameDiffMeta.double_diff(df1, df2))


def test_double_diff_2():
  print("Double Diff - 2")
  df1 = pd.DataFrame(np.array([[1,2], [4,5]]), columns=["a", "b"])
  df2 = pd.DataFrame(np.array([[3,1,2,4], [3,1,2,4], [3,4,5,5], [3,4,5,5]]), columns=["a", "b", "c", "d"])
  print(DataFrameDiffMeta.double_diff(df1, df2))


if __name__ == "__main__":
  test_col_diff()
  test_row_diff()
  test_double_diff_1()
  test_double_diff_2()
