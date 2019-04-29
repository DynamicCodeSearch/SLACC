import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import pandas as pd
import numpy as np
import warnings

from utils import lib, stat


warnings.filterwarnings("ignore")


class CellIndex(lib.O):
  def __init__(self, **kwargs):
    self.row = None
    self.col = None
    lib.O.__init__(self, **kwargs)

  def __repr__(self):
    return "(%d, %d)" % (self.row, self.col)

  def to_dict(self):
    return {
      "row": self.row,
      "col": self.col
    }

  @staticmethod
  def from_dict(d):
    if type(d) == dict:
      return CellIndex(row=d["row"], col=d["col"])
    return int(d)


class Range(lib.O):
  def __init__(self, **kwargs):
    self.start = None
    self.end = None
    lib.O.__init__(self, **kwargs)

  def to_dict(self):
    return {
      "start": self.start,
      "end": self.end
    }

  @staticmethod
  def from_dict(d):
    return Range(start=CellIndex.from_dict(d["start"]), end=CellIndex.from_dict(d["end"]))


class DataFrameRange(Range):
  def __init__(self, **kwargs):
    Range.__init__(self, **kwargs)

  def __repr__(self):
    return "dfRange {Start: %s, End: %s}" % (self.start, self.end)

  def to_dict(self):
    return {
      "start": self.start.to_dict(),
      "end": self.end.to_dict()
    }

  @staticmethod
  def from_dict(d):
    return DataFrameRange(start=CellIndex.from_dict(d["start"]), end=CellIndex.from_dict(d["end"]))


class ArrayRange(Range):
  def __init__(self, **kwargs):
    Range.__init__(self, **kwargs)

  def __repr__(self):
    return "arrayRange {Start: %s, End: %s}" % (self.start, self.end)

  @staticmethod
  def from_dict(d):
    return ArrayRange(start=CellIndex.from_dict(d["start"]), end=CellIndex.from_dict(d["end"]))


class MatrixRange(Range):
  def __init__(self, **kwargs):
    Range.__init__(self, **kwargs)

  def __repr__(self):
    return "matrixRange {Start: %s, End: %s}" % (self.start, self.end)

  def to_dict(self):
    return {
      "start": self.start.to_dict(),
      "end": self.end.to_dict()
    }

  @staticmethod
  def from_dict(d):
    return MatrixRange(start=CellIndex.from_dict(d["start"]), end=CellIndex.from_dict(d["end"]))


class DiffMeta(lib.O):
  def __init__(self, **kwargs):
    self.sim_score = None
    self.message = None
    self.types = None
    self.is_val1_empty = False
    self.is_val2_empty = False
    lib.O.__init__(self, **kwargs)

  def better(self, other):
    if other is None:
      return True
    return self.sim_score > other.sim_score

  def to_dict(self):
    return {
      "sim_score": self.sim_score,
      "message": self.message,
      "types": self.types,
      "is_val1_empty": self.is_val1_empty,
      "is_val2_empty": self.is_val2_empty
    }

  @staticmethod
  def from_dict(d):
    diff_type = d.get("diff_type", None)
    if diff_type == "array":
      return ArrayDiffMeta.from_dict(d)
    elif diff_type == "matrix":
      return MatrixDiffMeta.from_dict(d)
    elif diff_type == "dataFrame":
      return DataFrameDiffMeta.from_dict(d)
    else:
      types = None
      if "types" in d:
        types = (d["types"][0], d["types"][1])
      return DiffMeta(sim_score=d["sim_score"], message=d["message"], types=types,
                      is_val1_empty=d["is_val1_empty"], is_val2_empty=d["is_val2_empty"])


class ArrayDiffMeta(DiffMeta):
  def __init__(self, **kwargs):
    self.size_diff = None
    self.diff_type = "array"
    self.indices = None
    DiffMeta.__init__(self, **kwargs)

  def better(self, other):
    if other is None:
      return True
    if self.sim_score == other.sim_score:
      return self.size_diff < other.size_diff
    else:
      return self.sim_score > other.sim_score

  @staticmethod
  def difference(val1, val2):
    s1 = len(val1)
    s2 = len(val2)
    if val1.size == 0 or val2.size == 0:
      is_val1_empty = val1.size == 0
      is_val2_empty = val2.size == 0
      score = 1.0 if is_val1_empty and is_val2_empty else 0.0
      return ArrayDiffMeta(sim_score=score,
                           is_val1_empty=is_val1_empty,
                           is_val2_empty=is_val2_empty)
    elif s1 == s2:
      return ArrayDiffMeta(sim_score=ArrayDiffMeta.compute_sim_score(val1, val2), size_diff=0)
    else:
      return ArrayDiffMeta.compute_size_diff(val1, val2)

  @staticmethod
  def compute_size_diff(val1, val2):
    s1 = val1.shape
    s2 = val2.shape
    rev = False
    if s1[0] > s2[0]:
      val1, val2 = val2, val1
      s1, s2 = s2, s1
      rev = True
    s_diff = s2[0] - s1[0]
    best_score, indices = None, None
    for i in xrange(s_diff + 1):
      sub_array = val2[i:(i + s1[0])]
      score = ArrayDiffMeta.compute_sim_score(val1, sub_array)
      if not best_score or score > best_score:
        best_score = score
        meta1 = ArrayRange(start=0, end=s1[0])
        meta2 = ArrayRange(start=i, end=i+s1[0])
        indices = [meta1, meta2]
        if rev:
          indices = indices[::-1]
    return ArrayDiffMeta(sim_score=best_score, size_diff=s_diff, indices=indices)

  @staticmethod
  def compute_sim_score(v1, v2):
    assert v1.shape == v2.shape
    n_cells = len(v1)
    if n_cells == 0:
      return 1.0
    matches = sum([1 if v_i == v_j else 0 for v_i, v_j in zip(v1, v2)])
    return matches / n_cells

  def to_dict(self):
    indices = None
    if self.indices:
      indices = [index.to_dict() for index in self.indices]
    return {
      "sim_score": self.sim_score,
      "message": self.message,
      "size_diff": self.size_diff,
      "diff_type": self.diff_type,
      "indices": indices,
      "is_val1_empty": self.is_val1_empty,
      "is_val2_empty": self.is_val2_empty
    }

  @staticmethod
  def from_dict(d):
    indices = None
    if d.get("indices", None):
      indices = [ArrayRange.from_dict(index) for index in d["indices"]]
    return ArrayDiffMeta(sim_score=d["sim_score"], message=d["message"], size_diff=d["size_diff"],
                         diff_type=d["diff_type"], indices=indices,
                         is_val1_empty=d["is_val1_empty"], is_val2_empty=d["is_val2_empty"])


class MatrixDiffMeta(DiffMeta):
  def __init__(self, **kwargs):
    self.row_diff = None
    self.col_diff = None
    self.diff_type = "matrix"
    self.indices = None
    DiffMeta.__init__(self, **kwargs)

  def better(self, other):
    if other is None:
      return True
    if self.sim_score == other.sim_score:
      if self.row_diff == other.row_diff:
        return self.col_diff < other.col_diff
      elif self.col_diff == other.col_diff:
        return self.row_diff < other.row_diff
    else:
      return self.sim_score > other.sim_score

  @staticmethod
  def compute_sim_score(v1, v2):
    assert v1.shape == v2.shape
    n_cells = float(v1.shape[0] * v1.shape[1])
    if n_cells == 0:
      return 1.0
    matches = 0
    for i in xrange(v1.shape[0]):
      for j in xrange(v1.shape[1]):
        if v1[i][j] == v2[i][j]:
          matches += 1
    return matches / n_cells

  @staticmethod
  def difference(val1, val2):
    s1 = val1.shape
    s2 = val2.shape
    if val1.size == 0 and val2.size == 0:
      is_val1_empty = val1.size == 0
      is_val2_empty = val2.size == 0
      score = 1.0 if is_val1_empty and is_val2_empty else 0.0
      return MatrixDiffMeta(sim_score=score,
                            is_val1_empty=is_val1_empty,
                            is_val2_empty=is_val2_empty)
    elif s1 == s2:
      return MatrixDiffMeta(sim_score=MatrixDiffMeta.compute_sim_score(val1, val2),
                            row_diff=0, col_diff=0)
    elif s1[0] == s2[0]:
      return MatrixDiffMeta.compute_col_diff(val1, val2)
    elif s1[1] == s2[1]:
      return MatrixDiffMeta.compute_row_diff(val1, val2)
    else:
      return MatrixDiffMeta.compute_double_diff(val1, val2)

  @staticmethod
  def compute_col_diff(val1, val2):
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
      sub_matrix = val2[:, i:(i + c1)]
      score = MatrixDiffMeta.compute_sim_score(val1, sub_matrix)
      if not best_score or score > best_score:
        best_score = score
        meta1 = MatrixRange(start=CellIndex(row=0, col=0), end=CellIndex(row=s1[0], col=s1[1]))
        meta2 = MatrixRange(start=CellIndex(row=0, col=i), end=CellIndex(row=s2[0], col=i + c1))
        indices = [meta1, meta2]
        if rev:
          indices = indices[::-1]
    return MatrixDiffMeta(sim_score=best_score, row_diff=r_diff, col_diff=c_diff, indices=indices)

  @staticmethod
  def compute_row_diff(val1, val2):
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
      sub_matrix = val2[i:(i + r1), ]
      score = MatrixDiffMeta.compute_sim_score(val1, sub_matrix)
      if not best_score or score > best_score:
        best_score = score
        meta1 = MatrixRange(start=CellIndex(row=0, col=0), end=CellIndex(row=s1[0], col=s1[1]))
        meta2 = MatrixRange(start=CellIndex(row=i, col=0), end=CellIndex(row=i+r1, col=s2[1]))
        indices = [meta1, meta2]
        if rev:
          indices = indices[::-1]
    return MatrixDiffMeta(sim_score=best_score, row_diff=r_diff, col_diff=c_diff, indices=indices)

  @staticmethod
  def compute_double_diff(val1, val2):
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
      sub_matrix1 = val1[0:min(s1[0], s2[0]), :]
      sub_matrix2 = val2[0:min(s1[0], s2[0]), :]
      col_diff_meta = MatrixDiffMeta.compute_col_diff(sub_matrix1, sub_matrix2)
      sub_matrix1 = val1[:, 0:min(s1[1], s2[1])]
      sub_matrix2 = val2[:, 0:min(s1[1], s2[1])]
      row_diff_meta = MatrixDiffMeta.compute_row_diff(sub_matrix1, sub_matrix2)
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
        sub_matrix = val2[i:(i + s1[0]), j:(j + s1[1])]
        score = MatrixDiffMeta.compute_sim_score(val1, sub_matrix)
        if not best_score or score > best_score:
          best_score = score
          meta1 = MatrixRange(start=CellIndex(row=0, col=0), end=CellIndex(row=s1[0], col=s1[1]))
          meta2 = MatrixRange(start=CellIndex(row=i, col=j), end=CellIndex(row=i+s1[0], col=j+s1[1]))
          indices = [meta1, meta2]
          if rev:
            indices = indices[::-1]
    return MatrixDiffMeta(sim_score=best_score, row_diff=r_diff, col_diff=c_diff, indices=indices)

  def to_dict(self):
    indices = None
    if self.indices:
      indices = [index.to_dict() for index in self.indices]
    return {
      "sim_score": self.sim_score,
      "message": self.message,
      "row_diff": self.row_diff,
      "col_diff": self.col_diff,
      "diff_type": self.diff_type,
      "indices": indices,
      "is_val1_empty": self.is_val1_empty,
      "is_val2_empty": self.is_val2_empty
    }

  @staticmethod
  def from_dict(d):
    indices = None
    if d.get("indices", None):
      indices = [MatrixRange.from_dict(index) for index in d["indices"]]
    return MatrixDiffMeta(sim_score=d["sim_score"], message=d["message"],
                          row_diff=d["row_diff"], col_diff=d["col_diff"],
                          diff_type=d["diff_type"], indices=indices,
                          is_val1_empty=d["is_val1_empty"], is_val2_empty=d["is_val2_empty"])


class DataFrameDiffMeta(DiffMeta):
  def __init__(self, **kwargs):
    self.row_diff = None
    self.col_diff = None
    self.diff_type = "dataFrame"
    self.indices = None
    DiffMeta.__init__(self, **kwargs)

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
        return self.col_diff < other.col_diff
      elif self.col_diff == other.col_diff:
        return self.row_diff < other.row_diff
    else:
      return self.sim_score > other.sim_score

  @staticmethod
  def difference(val1, val2):
    s1 = val1.shape
    s2 = val2.shape
    if val1.empty or val2.empty:
      is_val1_empty = val1.empty
      is_val2_empty = val2.empty
      score = 1.0 if is_val1_empty and is_val2_empty else 0.0
      return DataFrameDiffMeta(sim_score=score,
                               is_val1_empty=is_val1_empty,
                               is_val2_empty=is_val2_empty)
    elif s1 == s2:
      return DataFrameDiffMeta(sim_score=DataFrameDiffMeta.compute_sim_score(val1, val2),
                               row_diff=0, col_diff=0)
    elif s1[0] == s2[0]:
      return DataFrameDiffMeta.compute_col_diff(val1, val2)
    elif s1[1] == s2[1]:
      return DataFrameDiffMeta.compute_row_diff(val1, val2)
    else:
      return DataFrameDiffMeta.compute_double_diff(val1, val2)

  @staticmethod
  def compute_col_diff(val1, val2):
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
      score = DataFrameDiffMeta.compute_sim_score(val1, sub_df)
      if not best_score or score > best_score:
        best_score = score
        meta1 = DataFrameRange(start=CellIndex(row=0, col=0), end=CellIndex(row=s1[0], col=s1[1]))
        meta2 = DataFrameRange(start=CellIndex(row=0, col=i), end=CellIndex(row=s2[0], col=i + c1))
        indices = [meta1, meta2]
        if rev:
          indices = indices[::-1]
    return DataFrameDiffMeta(sim_score=best_score, row_diff=r_diff, col_diff=c_diff, indices=indices)

  @staticmethod
  def compute_row_diff(val1, val2):
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
      score = DataFrameDiffMeta.compute_sim_score(val1, sub_df)
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

  @staticmethod
  def compute_double_diff(val1, val2):
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
      col_diff_meta = DataFrameDiffMeta.compute_col_diff(sub_df1, sub_df2)
      sub_df1 = val1.iloc[:, 0:min(s1[1], s2[1])]
      sub_df2 = val2.iloc[:, 0:min(s1[1], s2[1])]
      row_diff_meta = DataFrameDiffMeta.compute_row_diff(sub_df1, sub_df2)
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
        score = DataFrameDiffMeta.compute_sim_score(val1, sub_df)
        if not best_score or score > best_score:
          best_score = score
          meta1 = DataFrameRange(start=CellIndex(row=0, col=0), end=CellIndex(row=s1[0], col=s1[1]))
          meta2 = DataFrameRange(start=CellIndex(row=i, col=j), end=CellIndex(row=i+s1[0], col=j+s1[1]))
          indices = [meta1, meta2]
          if rev:
            indices = indices[::-1]
    return DataFrameDiffMeta(sim_score=best_score, row_diff=r_diff, col_diff=c_diff, indices=indices)

  @staticmethod
  def compute_sim_score(v1, v2):
    return MatrixDiffMeta.compute_sim_score(v1.values, v2.values)

  def to_dict(self):
    indices = None
    if self.indices:
      indices = [index.to_dict() for index in self.indices]
    return {
      "sim_score": self.sim_score,
      "message": self.message,
      "row_diff": self.row_diff,
      "col_diff": self.col_diff,
      "diff_type": self.diff_type,
      "indices": indices,
      "is_val1_empty": self.is_val1_empty,
      "is_val2_empty": self.is_val2_empty
    }

  @staticmethod
  def from_dict(d):
    indices = None
    if d.get("indices", None):
      indices = [MatrixRange.from_dict(index) for index in d["indices"]]
    return DataFrameDiffMeta(sim_score=d["sim_score"], message=d["message"],
                             row_diff=d["row_diff"], col_diff=d["col_diff"],
                             diff_type=d["diff_type"], indices=indices,
                             is_val1_empty=d["is_val1_empty"], is_val2_empty=d["is_val2_empty"])


def _test_array_diff():
  x = np.array([1, 2, 3, 4, 5])
  y = np.array([2, 3, 4])
  diff = ArrayDiffMeta.difference(x, y)
  print(diff)
  print(DiffMeta.from_dict(diff.to_dict()))
  print("####\n")


def _test_matrix_diff():
  x = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])
  y = np.array([[6, 7],
                [10, 11]])
  diff = MatrixDiffMeta.difference(x, y)
  print(diff)
  print(DiffMeta.from_dict(diff.to_dict()))
  print("####\n")


def _test_df_diff():
  x = pd.DataFrame([[1,2],[3,4]])
  y = pd.DataFrame()
  diff = DataFrameDiffMeta.difference(x, y)
  print(DiffMeta.from_dict(diff.to_dict()))


if __name__ == "__main__":
  _test_array_diff()
  _test_matrix_diff()
  _test_df_diff()
