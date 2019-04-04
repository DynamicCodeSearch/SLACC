import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


import pandas as pd
import numpy as np
import re

from utils import lib, stat


class CellIndex(lib.O):
  def __init__(self, **kwargs):
    self.row = None
    self.col = None
    lib.O.__init__(self, **kwargs)

  def __repr__(self):
    return "(%d, %d)" % (self.row, self.col)


class DataFrameRange(lib.O):
  def __init__(self, **kwargs):
    self.start = None
    self.end = None
    lib.O.__init__(self, **kwargs)

  def __repr__(self):
    return "dfRange {Start: %s, End: %s}" % (self.start, self.end)


class DataFrameDiffMeta(lib.O):
  def __init__(self, **kwargs):
    self.sim_score = None
    self.row_diff = 0.0
    self.col_diff = 0.0
    self.indices = None
    self.message = None
    lib.O.__init__(self, **kwargs)

  @staticmethod
  def aggregate(d_metas):
    aggregated = DataFrameDiffMeta()
    aggregated.sim_score = []
    aggregated.row_diff = []
    aggregated.col_diff = []
    for d_meta in d_metas:
      if d_meta.sim_score is not None:
        aggregated.sim_score.append(d_meta.sim_score)
        aggregated.row_diff.append(d_meta.row_diff)
        aggregated.col_diff.append(d_meta.col_diff)
    aggregated.sim_score = stat.Stat(aggregated.sim_score).report()
    aggregated.row_diff = stat.Stat(aggregated.row_diff).report()
    aggregated.col_diff = stat.Stat(aggregated.col_diff).report()
    return aggregated

  def better(self, other):
    if other is None:
      return True
    if self.sim_score == other.sim_score:
      if self.row_diff == other.row_diff:
        return self.col_diff > other.col_diff
      elif self.col_diff == other.col_diff:
        return self.row_diff > other.row_diff
    else:
      return self.sim_score > other.sim_score


def sim_score(v1, v2):
  assert v1.shape == v2.shape
  n_cells = float(v1.shape[0] * v1.shape[1])
  return np.sum(v1.values == v2.values) / n_cells


def col_diff(val1, val2):
  s1 = val1.shape
  s2 = val2.shape
  assert s1[0] == s2[0]
  rev = False
  if s1[1] > s2[1]:
    val1, val2 = val2, val1
    s1, s2 = s2, s1
    rev = True
  c1, c2 = s1[1], s2[1]
  r_diff = 0
  c_diff = c2 - c1
  best_score = None
  indices = None
  for i in xrange(c_diff + 1):
    sub_df = val2.iloc[:, i:(i + c1)]
    score = sim_score(val1, sub_df)
    if not best_score or score > best_score:
      best_score = score
      meta1 = DataFrameRange(start=CellIndex(row=0, col=0), end=CellIndex(row=s1[0], col=s1[1]))
      meta2 = DataFrameRange(start=CellIndex(row=0, col=i), end=CellIndex(row=s2[0], col=i + c1))
      indices = [meta1, meta2]
      if rev:
        indices = indices[::-1]
  return DataFrameDiffMeta(sim_score=best_score, row_diff=r_diff, col_diff=c_diff, indices=indices)


def row_diff(val1, val2):
  s1 = val1.shape
  s2 = val2.shape
  assert s1[1] == s2[1]
  rev = False
  if s1[0] > s2[0]:
    val1, val2 = val2, val1
    s1, s2 = s2, s1
    rev = True
  r1, r2 = s1[0], s2[0]
  r_diff = r2 - r1
  c_diff = 0
  best_score = None
  indices = None
  for i in xrange(r_diff + 1):
    sub_df = val2.iloc[i:(i + r1), ]
    sub_df.index = pd.RangeIndex(len(sub_df.index))
    score = sim_score(val1, sub_df)
    # print("************")
    # print(val1)
    # print(sub_df)
    # print(val1.shape, sub_df.shape)
    # print(np.sum(val1.values == sub_df.values))
    # print(sim_score(val1, sub_df))
    # exit()
    if not best_score or score > best_score:
      best_score = score
      meta1 = DataFrameRange(start=CellIndex(row=0, col=0), end=CellIndex(row=s1[0], col=s1[1]))
      meta2 = DataFrameRange(start=CellIndex(row=i, col=0), end=CellIndex(row=i+r1, col=s2[1]))
      indices = [meta1, meta2]
      if rev:
        indices = indices[::-1]
  return DataFrameDiffMeta(sim_score=best_score, row_diff=r_diff, col_diff=c_diff, indices=indices)


def double_diff(val1, val2):
  s1 = val1.shape
  s2 = val2.shape
  rev = False
  if s1[0] >= s2[0] and s1[1] >= s2[1]:
    val1, val2 = val2, val1
    s1, s2 = s2, s1
    rev = True
  elif s1[0] <= s2[0] and s1[1] <= s2[1]:
    pass
  else:
    sub_df1 = val1.iloc[0:min(s1[0], s2[0]), :]
    sub_df2 = val2.iloc[0:min(s1[0], s2[0]), :]
    col_diff_meta = col_diff(sub_df1, sub_df2)
    sub_df1 = val1.iloc[:, 0:min(s1[1], s2[1])]
    sub_df2 = val2.iloc[:, 0:min(s1[1], s2[1])]
    row_diff_meta = row_diff(sub_df1, sub_df2)
    if col_diff_meta.better(row_diff_meta):
      return col_diff_meta
    else:
      return row_diff_meta
  r_diff = s2[0] - s1[0]
  c_diff = s2[1] - s1[1]
  best_score = None
  indices = None
  for i in xrange(r_diff + 1):
    for j in xrange(c_diff + 1):
      sub_df = val2.iloc[i:(i + s1[0]), j:(j + s1[1])]
      score = sim_score(val1, sub_df)
      if not best_score or score > best_score:
        meta1 = DataFrameRange(start=CellIndex(row=0, col=0), end=CellIndex(row=s1[0], col=s1[1]))
        meta2 = DataFrameRange(start=CellIndex(row=i, col=j), end=CellIndex(row=i+s1[0], col=j+s1[1]))
        indices = [meta1, meta2]
        if rev:
          indices = indices[::-1]
  return DataFrameDiffMeta(sim_score=best_score, row_diff=r_diff, col_diff=c_diff, indices=indices)


def difference(val1, val2):
  s1 = val1.shape
  s2 = val2.shape
  if s1 == s2:
    return DataFrameDiffMeta(sim_score=sim_score(val1, val2),
                             row_diff=0, col_diff=0)
  elif s1[0] == s2[0]:
    return col_diff(val1, val2)
  elif s1[1] == s2[1]:
    return row_diff(val1, val2)
  else:
    return double_diff(val1, val2)


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
  return sorted(list(col_names))


def test_col_diff():
  print("Col Diff")
  df1 = pd.DataFrame(np.array([[1,2,3], [4,5,6], [7,8,9]]), columns=["a", "b", "c"])
  df2 = pd.DataFrame(np.array([[5, 1,2,3], [3, 4,5,6], [7, 7,8,9]]), columns=["x","a", "b", "c"])
  print(col_diff(df1, df2))


def test_row_diff():
  print("Row Diff")
  df1 = pd.DataFrame(np.array([[1,2,3], [4,5,6], [7,8,9]]), columns=["a", "b", "c"])
  df2 = pd.DataFrame(np.array([[0,-1,-3], [1,2,3], [4,5,6], [7,8,9], [0,-1,-3]]), columns=["a", "b", "c"])
  print(row_diff(df1, df2))


def test_double_diff_1():
  print("Double Diff - 1")
  df1 = pd.DataFrame(np.array([[1,2,3,4], [4,5,6,7]]), columns=["a", "b", "c", "d"])
  df2 = pd.DataFrame(np.array([[3,4], [1,2], [4,5], [9,7], [3, 3]]), columns=["a", "b"])
  print(double_diff(df1, df2))


def test_double_diff_2():
  print("Double Diff - 2")
  df1 = pd.DataFrame(np.array([[1,2], [4,5]]), columns=["a", "b"])
  df2 = pd.DataFrame(np.array([[3,1,2,4], [3,1,2,4], [3,4,5,5], [3,4,5,5]]), columns=["a", "b", "c", "d"])
  print(double_diff(df1, df2))


if __name__ == "__main__":
  test_col_diff()
  test_row_diff()
  test_double_diff_1()
  test_double_diff_2()
