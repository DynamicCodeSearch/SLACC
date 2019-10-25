import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from zss import simple_distance as edit_distance, Node

from misconceptions.syntactics.grammar.python import pandas_parser
from misconceptions.syntactics.grammar.R import r_parser


_PY_PARSER = None
_R_PARSER = None

__DEBUG = False


def get_py_parser():
  global _PY_PARSER
  if _PY_PARSER is None:
    _PY_PARSER = pandas_parser()
  return _PY_PARSER


def get_R_parser():
  global _R_PARSER
  if _R_PARSER is None:
    _R_PARSER = r_parser()
  return _R_PARSER


def make_zss_tree(ast_node):
  if hasattr(ast_node, "data"):
    data = ast_node.data
  else:
    data = ast_node.type
    # data = "TOKEN"
  node = Node(data)
  if hasattr(ast_node, "children"):
    for child in ast_node.children:
      node.addkid(make_zss_tree(child))
  return node


def py_parse(py_snippet):
  parsed = get_py_parser().parse(py_snippet)
  if __DEBUG:
    print("Py Parsed: ", parsed)
  return make_zss_tree(parsed)


def r_parse(r_snippet):
  parsed = get_R_parser().parse(r_snippet)
  if __DEBUG:
    print("R Parsed: ", parsed)
  return make_zss_tree(parsed)


def tree_edit_distance(py_snippet, r_snippet):
  py_parsed = py_parse(py_snippet)
  if __DEBUG:
    print("Tree Py: ")
    print(py_parsed)
    print("")
  r_parsed = r_parse(r_snippet)
  if __DEBUG:
    print("Tree R: ")
    print(r_parsed)
    print("")
  return edit_distance(py_parsed, r_parsed)


def verify():
  from utils import cache
  misconceptions_path = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/src/main/python/misconceptions.xlsx"
  wb = cache.read_excel(misconceptions_path, read_only=True)
  # sheet = wb.get_sheet_by_name('HighSim-HighSyn')
  sheet = wb.get_sheet_by_name('LowSim-LowSyn')
  parser = pandas_parser()
  py_seen = {}
  r_seen = {}
  for i, row in enumerate(sheet.iter_rows()):
    if i == 0:
      continue
    r_snippet = row[0].value
    py_snippet = row[1].value
    if i >= 1:
      py_parsed = py_seen.get(py_snippet, None)
      if py_parsed is None:
        py_parsed = py_parse(py_snippet)
        py_seen[py_snippet] = py_parsed
      r_parsed = r_seen.get(r_snippet, None)
      if r_parsed is None:
        r_parsed = r_parse(r_snippet)
        r_seen[r_snippet] = r_parsed
      print(i, edit_distance(py_parsed, r_parsed))


def _test():
  py_snippet = "df['Cabin'].apply(lambda x: str(x)[0])"
  r_snippet = "mean(df$Fare)"
  print(tree_edit_distance(py_snippet, r_snippet))


if __name__ == "__main__":
  _test()
  # verify()
