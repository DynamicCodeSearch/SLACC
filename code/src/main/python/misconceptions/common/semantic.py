import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import numpy as np

from utils import logger
from utils.lib import O
from misconceptions.common import mongo_driver, props, differences


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


class SemanticSummary(O):
  def __init__(self, **kwargs):
    self.sim_score = None
    self.n_mismatched = 0
    self.size_diff = None
    self.row_diff = None
    self.col_diff = None
    self.n_val1_empty = 0
    self.n_val2_empty = 0
    self.n_both_empty = 0
    O.__init__(self, **kwargs)

  def update_summary(self, diff):
    if diff.message == "Mismatched types":
      self.n_mismatched += 1
      return
    elif isinstance(diff, differences.DataFrameDiffMeta) or isinstance(diff, differences.MatrixDiffMeta):
      if diff.row_diff is not None:
        if not self.row_diff: self.row_diff = []
        self.row_diff.append(diff.row_diff)
      if diff.col_diff is not None:
        if not self.col_diff: self.col_diff = []
        self.col_diff.append(diff.col_diff)
    elif isinstance(diff, differences.ArrayDiffMeta):
      if diff.size_diff is not None:
        if not self.size_diff: self.size_diff = []
        self.size_diff.append(diff.size_diff)
    self.n_both_empty += 1 if diff.is_val1_empty and diff.is_val2_empty else 0
    self.n_val1_empty += 1 if diff.is_val1_empty else 0
    self.n_val2_empty += 1 if diff.is_val2_empty else 0
    if not self.sim_score:
      self.sim_score = []
    self.sim_score.append(diff.sim_score)

  def summarize(self):
    report = {}
    if self.sim_score:
      report["semantic_score"] = np.mean(self.sim_score)
    report["n_mismatched"] = self.n_mismatched
    if self.row_diff:
      report["row_diff"] = np.mean(self.row_diff)
    if self.col_diff:
      report["col_diff"] = np.mean(self.col_diff)
    if self.size_diff:
      report["size_diff"] = np.mean(self.size_diff)
    report["n_both_empty"] = self.n_both_empty
    report["n_val1_empty"] = self.n_val1_empty
    report["n_val2_empty"] = self.n_val2_empty
    return report


def update_semantic_scores(start=0, end=None, log_interval=100, limit=0):
  store = mongo_driver.MongoStore(props.DATASET)
  diff_records = store.load_differences(additional_queries={"n_mismatched": {"$exists": False}}, limit=limit)
  n_records = diff_records.count()
  LOGGER.info("Retrieved %d records ..." % n_records)
  semantic_columns = ["semantic_score", "n_mismatched", "row_diff", "col_diff", "size_diff",
                      "n_both_empty", "n_val1_empty", "n_val2_empty"]
  store.create_semantic_indices(semantic_columns)
  for i, diff_record in enumerate(diff_records):
    if i < start or (end and i >= end):
      continue
    if (i + 1) % log_interval == 0:
      LOGGER.info("Processing semantic difference for %d / %d" % (i+1, n_records))
    summary = SemanticSummary()
    for d in diff_record["diff"]:
      diff = differences.DiffMeta.from_dict(d)
      summary.update_summary(diff)
    query = {"_id": diff_record["_id"]}
    updates = summary.summarize()
    store.update_difference(query, updates)


if __name__ == "__main__":
  update_semantic_scores()
