import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from collections import OrderedDict
import pandas as pd

from misconceptions.common import mongo_driver, props, syntactic
from utils import logger, stat


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def export_similar_differences(sim, syn, xl_writer, sheet_name):
  LOGGER.info("Running for %s ... " % sheet_name)
  query = {"n_both_empty": {"$eq": 0}}
  if sim > 0:
    query["semantic_score"] = {"$gte": abs(sim)}
  elif sim < 0:
    query["semantic_score"] = {"$lte": abs(sim)}
  if syn > 0:
    query["d_levenshtein"] = {"$gte": abs(syn)}
  elif syn < 0:
    query["d_levenshtein"] = {"$lte": abs(syn)}
  projections = {"py_id": 1,
                 "r_id": 1,
                 "r_snippet": 1,
                 "r_return": 1,
                 "py_return": 1,
                 "py_snippet": 1,
                 "_id": 0,
                 "row_diff": 1,
                 "col_diff": 1,
                 "d_levenshtein": 1,
                 "size_diff": 1,
                 "semantic_score": 1}
  store = mongo_driver.MongoStore(props.DATASET)
  diffs = store.load_differences(additional_queries=query, projection=projections)
  r_stmts = []
  py_stmts = []
  syntactics = []
  semantics = []
  row_diffs = []
  col_diffs = []
  size_diffs = []
  for diff in diffs:
    # if diff["r_return"] == props.AUTO_RETURN:
    #   r_stmts.append(diff["r_snippet"])
    # else:
    #   r_stmts.append("%s; %s" % (diff["r_snippet"], diff["r_return"]))
    # if diff["py_return"] == props.AUTO_RETURN:
    #   py_stmts.append(diff["py_snippet"])
    # elif diff["py_return"] == props.SELF:
    #   py_stmts.append("return %s" % diff["py_snippet"])
    # else:
    #   py_stmts.append("%s; return %s" % (diff["py_snippet"], diff["py_return"]))
    r_stmt = syntactic.r_normalize(store.load_stmt(diff["r_id"])).replace(syntactic.RENAMED_VARIABLE, "df")
    py_stmt = syntactic.py_normalize(store.load_stmt(diff["py_id"])).replace(syntactic.RENAMED_VARIABLE, "df")
    r_stmts.append(r_stmt)
    py_stmts.append(py_stmt)
    syntactics.append(diff.get("d_levenshtein", None))
    semantics.append(diff.get("semantic_score", None))
    row_diffs.append(diff.get("row_diff", None))
    col_diffs.append(diff.get("col_diff", None))
    size_diffs.append(diff.get("size_diff", None))
  d = OrderedDict()
  d["R"] = r_stmts
  d["Pandas"] = py_stmts
  d["Levenshtein"] = syntactics
  d["Semantic Score"] = semantics
  d["row_diff"] = row_diffs
  d["col_diff"] = col_diffs
  d["size_diff"] = size_diffs
  df = pd.DataFrame(d, columns=d.keys())
  df.to_excel(xl_writer, sheet_name=sheet_name, index=False)


def export_runner(xl_path):
  writer = pd.ExcelWriter(xl_path, engine='xlsxwriter')
  export_similar_differences(0.9, -19, writer, "HighSim-HighSyn")
  export_similar_differences(0.9, 19, writer, "HighSim-LowSyn")
  export_similar_differences(-0.1, -19, writer, "LowSim-HighSyn")
  export_similar_differences(-0.1, 39, writer, "LowSim-LowSyn")
  writer.save()
  writer.close()


if __name__ == "__main__":
  export_runner("misconceptions.xlsx")
