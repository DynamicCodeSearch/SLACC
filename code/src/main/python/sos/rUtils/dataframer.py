import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


import pandas as pd
import numpy as np

from utils import lib, stat


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
      indices = [(0, s1[1]), (i, i + c1)]
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
      indices = [(0, s1[0]), (i, i + r1)]
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
    return DataFrameDiffMeta(sim_score=None, row_diff=abs(s1[0] - s2[0]), col_diff=abs(s1[1] - s2[1]),
                             indices=None, message="Significant difference between two dataframes")


def test_col_diff():
  df1 = pd.DataFrame(np.array([[1,2,3], [4,5,6], [7,8,9]]), columns=["a", "b", "c"])
  df2 = pd.DataFrame(np.array([[5, 1,2,3], [3, 4,5,6], [7, 7,8,9]]), columns=["x","a", "b", "c"])
  print(col_diff(df1, df2))


def test_row_diff():
  df1 = pd.DataFrame(np.array([[1,2,3], [4,5,6], [7,8,9]]), columns=["a", "b", "c"])
  df2 = pd.DataFrame(np.array([[0,-1,-3], [1,2,3], [4,5,6], [7,8,9], [0,-1,-3]]), columns=["a", "b", "c"])
  print(row_diff(df1, df2))


if __name__ == "__main__":
  # test_col_diff()
  test_row_diff()

