import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import asttokens
import astor
import Levenshtein
import tokenize
import io
from rpy2 import rinterface

from utils import logger, stat
from analysis.parsers import parser
from misconceptions.common import compare, mongo_driver, props, datatypes
from misconceptions.rUtils import functions
from misconceptions.syntactics import distances as ast_distances

R_PARSER_PATH = os.path.join(props.CODE_SRC, "r", "parser", "r_parser.R")
LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))
RENAMED_VARIABLE = "slacc"
_REPLACE_VARIABLE_FUNC = None


def get_replace_variable_func():
  global _REPLACE_VARIABLE_FUNC
  if not _REPLACE_VARIABLE_FUNC:
    _REPLACE_VARIABLE_FUNC = functions.get_r_function(R_PARSER_PATH, "replace_variable_name")
  return _REPLACE_VARIABLE_FUNC


def normalize(stmt):
  if stmt["language"] == props.TYPE_R:
    return r_normalize(stmt).strip()
  elif stmt["language"] == props.TYPE_PYTHON:
    return py_normalize(stmt).strip()
  else:
    raise RuntimeError("WTF! Unknown language: %s" % stmt["language"])


def r_normalize(stmt):
  return normalize_R_snippet(stmt["snippet"], str(stmt["variables"][0]))


def py_normalize(stmt):
  return PyVariableRenamer(stmt["snippet"], str(stmt["variables"][0])).parse()


def normalize_R_snippet(snippet, variable):
  r_func = get_replace_variable_func()
  try:
    return datatypes.convert_r_object_to_py(r_func(snippet, variable))[0].strip()
  except rinterface.RRuntimeError:
    return None


def gen_tokens(snippet):
  tokens = []
  for tok_type, tok, (srow, scol), (erow, ecol), line in tokenize.generate_tokens(io.BytesIO(snippet.encode('utf-8')).readline):
    if tok_type == 0:
      return tokens
    tokens.append(tok)
  return tokens


def py_lexer(py_snippet):
  return gen_tokens(py_snippet)


def r_lexer(r_snippet):
  r_tokens = []
  for tok in gen_tokens(r_snippet):
    if tok == '-' and r_tokens and r_tokens[-1] == '<':
      r_tokens[-1] = '<-'
    else:
      r_tokens.append(tok)
  return r_tokens


def n_gram_distance(py_snippet, r_snippet):

  def _n_gram_helper(p_toks, r_toks):
    assert len(p_toks) == len(r_toks)
    #
    # def _get_num_mismatches(s):
    #   num_mismatches = 0
    #   for p, r in zip(p_toks[s:s+n], r_toks[s:s+n]):
    #     if p != r:
    #       num_mismatches += 1
    #   return num_mismatches
    # total_dist = 0
    # for i in xrange(len(p_toks)):
    #   total_dist += _get_num_mismatches(i)
    # return total_dist
    num_mismatches = 0
    for p, r in zip(p_toks, r_toks):
      if p != r:
        num_mismatches += 1
    return num_mismatches

  py_tokens = py_lexer(py_snippet)
  r_tokens = r_lexer(r_snippet)
  is_reversed = False
  if len(py_tokens) == len(r_tokens):
    return _n_gram_helper(py_tokens, r_tokens) / float(len(py_tokens)), (0, len(py_tokens)), (0, len(r_tokens))
  elif len(py_tokens) < len(r_tokens):
    is_reversed = True
    py_tokens, r_tokens = r_tokens, py_tokens
  best_similarity, best_start = None, None
  delta = len(py_tokens) - len(r_tokens)
  for start in xrange(delta):
    similarity = _n_gram_helper(py_tokens[start:len(r_tokens) + start], r_tokens)
    if best_similarity is None or similarity < best_similarity:
      best_similarity = similarity
      best_start = start
  if is_reversed:
    return (best_similarity + delta) / float(len(py_tokens)), py_snippet, "".join(py_tokens[best_start:best_start+len(r_tokens)])
  return (best_similarity + delta) / float(len(py_tokens)), "".join(py_tokens[best_start:best_start+len(r_tokens)]), r_snippet


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


def fetch_snippets(language=None, use_normalized=False):
  store = mongo_driver.MongoStore(props.DATASET)
  stmts = {}
  mongo_stmts = store.load_valid_snippets(language=language, use_normalized=use_normalized)
  for mongo_stmt in mongo_stmts:
    stmt = compare.Statement(mongo_id=mongo_stmt["_id"], snippet=mongo_stmt["snippet"],
                             variables=mongo_stmt["variables"], language=language)
    stmts[stmt.mongo_id] = stmt
  return stmts


def get_normalized_py_statements(debug=False):
  stmts = fetch_snippets(language=props.TYPE_PYTHON, use_normalized=True)
  LOGGER.info("Retrieved %d python statements ... " % len(stmts))
  normalized = []
  for i, (stmt_id, stmt) in enumerate(stmts.items()):
    assert stmt.variables and len(stmt.variables) == 1
    if debug and len(normalized) % 100 == 0:
      LOGGER.info("Processing %d py snippet ... " % len(normalized))
    stmt.normalized = PyVariableRenamer(stmt.snippet, stmt.variables[0]).parse()
    if stmt.normalized:
      stmt.normalized = stmt.normalized.replace("slacc", "df")
    normalized.append(stmt)
  return normalized


def get_normalized_R_statements(debug=False):
  stmts = fetch_snippets(language=props.TYPE_R, use_normalized=True)
  LOGGER.info("Retrieved %d R statements ... " % len(stmts))
  normalized = []
  for i, (stmt_id, stmt) in enumerate(stmts.items()):
    if debug and i % 100 == 0:
      LOGGER.info("Processing %d / %d R snippet ... " % (i + 1, len(stmts)))
    assert stmt.variables and len(stmt.variables) == 1
    stmt.normalized = normalize_R_snippet(stmt.snippet, str(stmt.variables[0]))
    if stmt.normalized:
      stmt.normalized = stmt.normalized.replace("slacc", "df")
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
                 "d_jaro": 1,
                 "d_jaro_winkler": 1,
                 "d_ast": 1,
                 "d_levenshtein": 1,
                 "size_diff": 1,
                 "semantic_score": 1}
  store = mongo_driver.MongoStore(props.DATASET)
  asts, levenshteins, jaros, jaro_winklers, n_grams = [], [], [], [], []
  semantics = []
  i = 0
  for diff in store.load_differences(projection=projections):
    i += 1
    if i % 10000 == 0:
      LOGGER.info("Processing diff : %d", i)
    levenstein = diff.get("d_levenshtein", None)
    ast = diff.get("d_ast", None)
    jaro = diff.get("d_jaro", None)
    jaro_winkler = diff.get("d_jaro_winkler", None)
    n_gram = diff.get("d_n_gram", None)
    semantic = diff.get("semantic_score", None)
    if levenstein is not None:
      levenshteins.append(levenstein)
    if ast is not None:
      asts.append(ast)
    if jaro is not None:
      jaros.append(jaro)
    if jaro_winkler is not None:
      jaro_winklers.append(jaro_winkler)
    if n_gram is not None:
      n_grams.append(n_gram)
    if semantic is not None:
      semantics.append(semantic)
  print("### N Gram distance")
  print(stat.Stat(n_grams).report())
  print("### Levenshtein distance")
  print(stat.Stat(levenshteins).report())
  print("### Jaro distance")
  print(stat.Stat(jaros).report())
  print("### Jaro-Winkler distance")
  print(stat.Stat(jaro_winklers).report())
  print("### AST distance")
  print(stat.Stat(asts).report())
  print("### Semantics")
  print(stat.Stat(semantics).report())


def update_syntactic_distances(start=None, end=None):
  store = mongo_driver.MongoStore(props.DATASET)
  r_stmts = get_normalized_R_statements()
  py_stmts = get_normalized_py_statements()
  start_found = False
  LOGGER.info("Running between the range start: %d and end: %d" % (start, end))
  for i, r_stmt in enumerate(r_stmts):
    if (start is not None and i < start) or (end is not None and i > end):
      continue
    if not start_found:
      all_r_cursor = store.load_differences(r_id=r_stmt.mongo_id, projection={"outputs": False})
      # n_processed = sum([1 if "d_jaro" in s else 0 for s in all_r_cursor])
      # all_r_filter_cursor = store.load_differences(r_id=r_stmt.mongo_id,
      #                                              additional_queries={"d_n_gram": {"$exists": True}},
      #                                              projection={"diff": False})
      # if all_r_cursor.count() == all_r_filter_cursor.count():
      #   LOGGER.info("Processed %d / %d R snippet !" % (i + 1, len(r_stmts)))
      #   continue
      start_found = True
    if not r_stmt.normalized:
      continue
    r_tree = ast_distances.r_parse(r_stmt.normalized)
    LOGGER.info("Processing %d / %d R snippet ... " % (i + 1, len(r_stmts)))
    py_trees = {}
    for j, py_stmt in enumerate(py_stmts):
      if r_stmt.normalized and py_stmt.normalized:
        py_tree = py_trees.get(j, None)
        if not py_tree:
          py_tree = ast_distances.py_parse(py_stmt.normalized)
          py_trees[j] = py_tree
        updates = {
          "r_snippet": r_stmt.snippet,
          "py_snippet": py_stmt.snippet,
          "d_levenshtein": levenshtein(r_stmt.normalized, py_stmt.normalized),
          "d_jaro": jaro(r_stmt.normalized, py_stmt.normalized),
          "d_jaro_winkler": jaro_winkler(r_stmt.normalized, py_stmt.normalized),
          "d_ast": ast_distances.edit_distance(py_tree, r_tree)
        }
        try:
          updates["d_n_gram"] = n_gram_distance(r_stmt.normalized, py_stmt.normalized)[0]
        except Exception as e:
          updates["d_n_gram"] = 1.0
        query = {"r_id": r_stmt.mongo_id, "py_id": py_stmt.mongo_id}
        store.update_difference(query, updates)


def update_ngram_distance():
  store = mongo_driver.MongoStore(props.DATASET)
  diffs = store.load_differences(projection={"diff": False})


def get_top_syntax():
  store = mongo_driver.MongoStore(props.DATASET)
  diffs = store.load_differences(projection={"diff": False})
  print(diffs.count())
  for i, diff in enumerate(diffs):
    if i % 1000 == 0:
      print(i)


def _test():
  r_snippet = """
  static String join_j(String delimiter, List<String> arr) { 
    return delimiter.join("", arr);
  }
  """
  py_snippet = """
  def join_p(delimiter, arr):
    return delimiter.join(arr)
  """
  print("Levenshtein:", levenshtein(r_snippet, py_snippet))
  print("Jaro:", jaro(r_snippet, py_snippet))
  print("Jaro-Winkler:", jaro_winkler(r_snippet, py_snippet))
  x = 'ASASD DADsa Adasdsad'


def _test_tokenize():
  py_snippet = "numpy.mean(df, axis==5.0)"
  r_snippet = "mean(df)"
  print(n_gram_distance(py_snippet, r_snippet))


def _update_syntactic_distances():
  args = sys.argv
  end = int(args[2]) if len(args) >= 3 else None
  start = int(args[1]) if len(args) >= 2 else None
  update_syntactic_distances(start=start, end = end)


def test_normalized_asts_R():
  r_stmts = get_normalized_R_statements()
  for i, r_stmt in enumerate(r_stmts):
    if not r_stmt.normalized:
      continue
    print(i, r_stmt.normalized)
    r_tree = ast_distances.r_parse(r_stmt.normalized)


def test_normalized_asts_py():
  py_stmts = get_normalized_py_statements()
  for i, py_stmt in enumerate(py_stmts):
    if not py_stmt.normalized:
      continue
    print(i, py_stmt.normalized)
    py_tree = ast_distances.py_parse(py_stmt.normalized)


if __name__ == "__main__":
  _test()
  # _test_tokenize()
  # test_distance_distribution()
  # _update_syntactic_distances()
  # test_normalized_asts_R()
  # test_normalized_asts_py()
  # get_top_syntax()
