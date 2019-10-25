import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from utils import logger
from misconceptions.common import mongo_driver, props
from misconceptions.common import syntactic
from misconceptions.syntactics import distances as ast_distances

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def syntactic_differences(start=0):
  store = mongo_driver.MongoStore(props.DATASET)
  stmts = syntactic.get_normalized_R_statements(debug=True)
  trees = {}
  for i in xrange(len(stmts)-1):
    if i < start:
      continue
    LOGGER.info("Processing %d / %d R snippet ... " % (i + 1, len(stmts)))
    stmt_i = stmts[i]
    if not stmt_i.normalized:
      continue
    stmt_i_tree = trees.get(i, None)
    if not stmt_i_tree:
      stmt_i_tree = ast_distances.r_parse(stmt_i.normalized)
      trees[i] = stmt_i_tree
    records = []
    for j in xrange(i+1, len(stmts)):
      if i >= j:
        continue
      stmt_j = stmts[j]
      if not stmt_j.normalized:
        continue
      stmt_j_tree = trees.get(j, None)
      if not stmt_j_tree:
        stmt_j_tree = ast_distances.r_parse(stmt_j.normalized)
        trees[j] = stmt_j_tree
      record = {
        "id_1": stmt_i.mongo_id,
        "id_2": stmt_j.mongo_id,
        "language": props.TYPE_R,
        "d_levenshtein": syntactic.levenshtein(stmt_i.normalized, stmt_j.normalized),
        "d_jaro": syntactic.jaro(stmt_i.normalized, stmt_j.normalized),
        "d_jaro_winkler": syntactic.jaro_winkler(stmt_i.normalized, stmt_j.normalized),
        "d_ast": ast_distances.edit_distance(stmt_i_tree, stmt_j_tree)
      }
      try:
        record["d_n_gram"] = syntactic.n_gram_distance(stmt_i.normalized, stmt_j.normalized)[0]
      except Exception as e:
        record["d_n_gram"] = 1.0
      records.append(record)
    store.save_self_syntactic_differences(records, do_log=True)

def test():
  stmts = syntactic.get_normalized_R_statements(debug=True)
  print(ast_distances.r_parse(stmts[0].normalized))


if __name__ == "__main__":
  syntactic_differences()
  # test()
