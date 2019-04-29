import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import asttokens
import astor
import Levenshtein
from rpy2 import rinterface

from utils import logger, stat
from analysis.parsers import parser
from misconceptions.common import compare, mongo_driver, props, datatypes
from misconceptions.pdUtils import crawler
from misconceptions.rUtils import functions

R_PARSER_PATH = os.path.join(props.CODE_SRC, "r", "parser", "r_parser.R")
LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))
RENAMED_VARIABLE = "slacc"
_REPLACE_VARIABLE_FUNC = None


def get_replace_variable_func():
  global _REPLACE_VARIABLE_FUNC
  if not _REPLACE_VARIABLE_FUNC:
    _REPLACE_VARIABLE_FUNC = functions.get_r_function(R_PARSER_PATH, "replace_variable_name")
  return _REPLACE_VARIABLE_FUNC


def normalize_R_snippet(snippet, variable):
  r_func = get_replace_variable_func()
  try:
    return datatypes.convert_r_object_to_py(r_func(snippet, variable))[0].strip()
  except rinterface.RRuntimeError:
    return None


class PyVariableRenamer(parser.Traveller):
  def __init__(self, src, variable):
    self.src = src
    self.variable = variable
    self.ast_tokenized = None
    parser.Traveller.__init__(self)

  def parse(self):
    self.ast_tokenized = asttokens.ASTTokens(self.src, parse=True)
    self.visit(self.ast_tokenized.tree)
    return astor.to_source(self.ast_tokenized.tree).strip()

  def visit_Name(self, node, meta):
    if node.id == self.variable:
      node.id = RENAMED_VARIABLE


def fetch_snippets(language=None):
  store = mongo_driver.MongoStore(props.DATASET)
  stmts = {}
  mongo_stmts = store.load_valid_snippets(language=language)
  for mongo_stmt in mongo_stmts:
    stmt = compare.Statement(mongo_id=mongo_stmt["_id"], snippet=mongo_stmt["snippet"],
                             variables=mongo_stmt["variables"], language=language)
    stmts[stmt.mongo_id] = stmt
  return stmts


def get_normalized_py_statements(debug=False):
  stmts = fetch_snippets(language=props.TYPE_PYTHON)
  LOGGER.info("Retrieved %d python statements ... " % len(stmts))
  top_py_stmts = crawler.get_stmt_counts(props.PY_STMT_LIMIT)
  normalized = []
  for i, (stmt_id, stmt) in enumerate(stmts.items()):
    assert stmt.variables and len(stmt.variables) == 1
    if stmt.snippet not in top_py_stmts:
      continue
    if debug and len(normalized) % 100 == 0:
      LOGGER.info("Processing %d py snippet ... " % len(normalized))
    stmt.normalized = PyVariableRenamer(stmt.snippet, stmt.variables[0]).parse()
    normalized.append(stmt)
  return normalized


def get_normalized_R_statements(debug=False):
  stmts = fetch_snippets(language=props.TYPE_R)
  LOGGER.info("Retrieved %d R statements ... " % len(stmts))
  normalized = []
  for i, (stmt_id, stmt) in enumerate(stmts.items()):
    if debug and i % 100 == 0:
      LOGGER.info("Processing %d / %d R snippet ... " % (i + 1, len(stmts)))
    assert stmt.variables and len(stmt.variables) == 1
    stmt.normalized = normalize_R_snippet(stmt.snippet, str(stmt.variables[0]))
    normalized.append(stmt)
  return normalized


def levenshtein(r_snippet, py_snippet):
  return Levenshtein.distance(r_snippet, py_snippet)


def hamming(r_snippet, py_snippet):
  return Levenshtein.hamming(r_snippet, py_snippet)


def jaro(r_snippet, py_snippet):
  return 1.0 - Levenshtein.jaro(r_snippet, py_snippet)


def jaro_winkler(r_snippet, py_snippet):
  return 1.0 - Levenshtein.jaro_winkler(r_snippet, py_snippet)


def test_distance_distribution():
  r_stmts = get_normalized_R_statements()
  py_stmts = get_normalized_py_statements()
  levenshteins, jaros, jaro_winklers = [], [], []
  for i, r_stmt in enumerate(r_stmts):
    LOGGER.info("Processing %d / %d R snippet ... " % (i + 1, len(r_stmts)))
    for py_stmt in py_stmts:
      levenshteins.append(levenshtein(r_stmt.normalized, py_stmt.normalized))
      jaros.append(jaro(r_stmt.normalized, py_stmt.normalized))
      jaro_winklers.append(jaro_winkler(r_stmt.normalized, py_stmt.normalized))
  print("### Levenshtein distance")
  print(stat.Stat(levenshteins).report())
  print("### Jaro distance")
  print(stat.Stat(jaros).report())
  print("### Jaro-Winkler distance")
  print(stat.Stat(jaro_winklers).report())


def update_syntactic_distances():
  store = mongo_driver.MongoStore(props.DATASET)
  r_stmts = get_normalized_R_statements()
  py_stmts = get_normalized_py_statements()
  start_found = False
  for i, r_stmt in enumerate(r_stmts):
    if not start_found:
      all_r_cursor = store.load_differences(r_id=r_stmt.mongo_id, projection={"outputs": False})
      # n_processed = sum([1 if "d_jaro" in s else 0 for s in all_r_cursor])
      all_r_filter_cursor = store.load_differences(r_id=r_stmt.mongo_id,
                                                   additional_queries={"d_jaro": {"$exists": True}},
                                                   projection={"outputs": False})
      if all_r_cursor.count() == all_r_filter_cursor.count():
        LOGGER.info("Processed %d / %d R snippet !" % (i + 1, len(r_stmts)))
        continue
      start_found = True
    LOGGER.info("Processing %d / %d R snippet ... " % (i + 1, len(r_stmts)))
    for j, py_stmt in enumerate(py_stmts):
      updates = {
        "r_snippet": r_stmt.snippet,
        "py_snippet": py_stmt.snippet,
        "d_levenshtein": levenshtein(r_stmt.normalized, py_stmt.normalized),
        "d_jaro": jaro(r_stmt.normalized, py_stmt.normalized),
        "d_jaro_winkler": jaro_winkler(r_stmt.normalized, py_stmt.normalized)
      }
      query = {"r_id": r_stmt.mongo_id, "py_id": py_stmt.mongo_id}
      store.update_difference(query, updates)


def get_top_syntax():
  store = mongo_driver.MongoStore(props.DATASET)
  diffs = store.load_differences(projection={"diff": False})
  print(diffs.count())
  for i, diff in enumerate(diffs):
    if i % 1000 == 0:
      print(i)


def _test():
  r_snippet = "select(df, A, B)"
  py_snippet = "df[['A', 'B']]"
  print("Levenshtein:", levenshtein(r_snippet, py_snippet))
  print("Jaro:", jaro(r_snippet, py_snippet))
  print("Jaro-Winkler:", jaro_winkler(r_snippet, py_snippet))


if __name__ == "__main__":
  # test_distance_distribution()
  update_syntactic_distances()
  # get_top_syntax()
