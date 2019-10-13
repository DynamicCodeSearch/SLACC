import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from collections import OrderedDict
import pandas as pd

from misconceptions.common import mongo_driver, props, syntactic
from utils import logger, cache


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def export_similar_differences(sim, syn, xl_writer, sheet_name, syn_key):
  LOGGER.info("Running for %s ... " % sheet_name)
  query = {"n_both_empty": {"$eq": 0}}
  if sim > 0:
    query["semantic_score"] = {"$gte": abs(sim)}
  elif sim < 0:
    query["semantic_score"] = {"$lte": abs(sim)}
  if syn > 0:
    query[syn_key] = {"$gte": abs(syn)}
  elif syn < 0:
    query[syn_key] = {"$lte": abs(syn)}
  projections = {"py_id": 1,
                 "r_id": 1,
                 "r_snippet": 1,
                 "r_return": 1,
                 "py_return": 1,
                 "py_snippet": 1,
                 "_id": 0,
                 "row_diff": 1,
                 "col_diff": 1,
                 "d_n_gram": 1,
                 "d_ast": 1,
                 "d_levenshtein": 1,
                 "size_diff": 1,
                 "semantic_score": 1}
  store = mongo_driver.MongoStore(props.DATASET)
  diffs = [d for d in store.load_differences(additional_queries=query, projection=projections)]
  r_stmts = []
  py_stmts = []
  n_grams = []
  levenshteins = []
  asts = []
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
    r_stmt = syntactic.r_normalize(store.load_stmt(diff["r_id"], use_normalized=True)).replace(syntactic.RENAMED_VARIABLE, "df")
    py_stmt = syntactic.py_normalize(store.load_stmt(diff["py_id"], use_normalized=True)).replace(syntactic.RENAMED_VARIABLE, "df")
    r_stmts.append(r_stmt)
    py_stmts.append(py_stmt)
    n_grams.append(diff.get("d_n_gram", None))
    levenshteins.append(diff.get("d_levenshtein", None))
    asts.append(diff.get("d_ast", None))
    semantics.append(diff.get("semantic_score", None))
    row_diffs.append(diff.get("row_diff", None))
    col_diffs.append(diff.get("col_diff", None))
    size_diffs.append(diff.get("size_diff", None))
  d = OrderedDict()
  d["R"] = r_stmts
  d["Pandas"] = py_stmts
  d["AST Distance"] = asts
  d["N-Gram Distance"] = n_grams
  d["Semantic Score"] = semantics
  d["row_diff"] = row_diffs
  d["col_diff"] = col_diffs
  d["size_diff"] = size_diffs
  df = pd.DataFrame(d, columns=d.keys())
  df.to_excel(xl_writer, sheet_name=sheet_name, index=False)


def export_runner_n_gram(xl_path):
  cache.mkdir(props.EXPORT_HOME)
  writer = pd.ExcelWriter(os.path.join(props.EXPORT_HOME, xl_path), engine='xlsxwriter')
  export_similar_differences(0.9, -0.91, writer, "HighSim-HighSyn", "d_n_gram")
  export_similar_differences(0.9, 0.91, writer, "HighSim-LowSyn", "d_n_gram")
  export_similar_differences(-0.1, -0.91, writer, "LowSim-HighSyn", "d_n_gram")
  export_similar_differences(-0.1, 0.91, writer, "LowSim-LowSyn", "d_n_gram")
  writer.save()
  writer.close()


def export_runner_levenshtein(xl_path):
  cache.mkdir(props.EXPORT_HOME)
  writer = pd.ExcelWriter(os.path.join(props.EXPORT_HOME, xl_path), engine='xlsxwriter')
  export_similar_differences(0.9, -28, writer, "HighSim-HighSyn", "d_levenshtein")
  export_similar_differences(0.9, 47, writer, "HighSim-LowSyn", "d_levenshtein")
  export_similar_differences(-0.1, -28, writer, "LowSim-HighSyn", "d_levenshtein")
  export_similar_differences(-0.1, 47, writer, "LowSim-LowSyn", "d_levenshtein")
  writer.save()
  writer.close()


def export_runner_ast(xl_path):
  cache.mkdir(props.EXPORT_HOME)
  writer = pd.ExcelWriter(os.path.join(props.EXPORT_HOME, xl_path), engine='xlsxwriter')
  export_similar_differences(0.9, -9, writer, "HighSim-HighSyn", "d_ast")
  export_similar_differences(0.9, 22, writer, "HighSim-LowSyn", "d_ast")
  export_similar_differences(-0.1, -9, writer, "LowSim-HighSyn", "d_ast")
  export_similar_differences(-0.1, 22, writer, "LowSim-LowSyn", "d_ast")
  writer.save()
  writer.close()


def export_normalized_stmt_file_map(xl_path):
  store = mongo_driver.MongoStore(props.DATASET)
  writer = pd.ExcelWriter(xl_path, engine='xlsxwriter')
  snippets = []
  languages = []
  file_names = []
  for file_stmt in store.load_stmt_file_map():
    snippet = file_stmt["snippet"].replace("slacc", "df")
    empties = [''] * (len(file_stmt["file_names"]) - 1)
    snippets += [snippet] + empties
    languages += [file_stmt["language"]] + empties
    file_names += file_stmt["file_names"]
  d = OrderedDict()
  d["snippet"] = snippets
  d["languages"] = languages
  d["file_names"] = file_names
  df = pd.DataFrame(d, columns=d.keys())
  df.to_excel(writer, sheet_name="Snippet File Map", index=False)


if __name__ == "__main__":
  export_runner_n_gram("misconceptions_n_gram.xlsx")
  export_runner_levenshtein("misconceptions_levenshtein.xlsx")
  export_runner_ast("misconceptions_ast.xlsx")
  # export_normalized_stmt_file_map("metadata.xlsx")
