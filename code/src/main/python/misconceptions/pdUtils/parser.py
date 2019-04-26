import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


from utils import lib, cache
from misconceptions.common import helper

import pandas as pd
import re
import inspect


# from lark import Lark, Visitor, Transformer, Tree
# GRAMMAR = """
#     start: subset+
#     subset: CNAME (rows | cols | iloc) -> expr
#
#     rows: "[" _index "]"
#     cols: "[" label ("," label)* "]" _STRING_INNER? NEWLINE
#     iloc: "." "iloc" (rows | _rows_cols)
#
#     _rows_cols: "[" left ("," right?)? "]"
#     left: _index
#     right: _index
#
#     _index: range | NUMBER
#     range: start_idx ":" end_idx
#     start_idx: NUMBER*
#     end_idx: NUMBER*
#     label: "'" CNAME "'" | ESCAPED_STRING
#     _STRING_INNER: /.+?/
#
#     %import common.CNAME -> CNAME
#     %import common.INT -> NUMBER
#     %import common.ESCAPED_STRING -> ESCAPED_STRING
#     %import common.WORD
#     %import common.WS
#     %import common.NEWLINE -> NEWLINE
#     %ignore WS
# """
#
#
# test_rows = """
#             df[0] df[0:1] df[10:100] df[:1] df[1:]
#             """
#
# test_cols = """
#             df[['a']] df[["aaa"]] df[['a', 'b', 'c']] df[['aaa', 'bbb', 'ccc']]
#
#             """
#
# test_iloc_rows = """
#                  df.iloc[1] df.iloc[1, ] df.iloc[:] df.iloc[0:] df.iloc[:1]
#                  df.iloc[0:1] df.iloc[0:1, 0:1] df.iloc[0:, 0:] df.iloc[:1, :1]
#                  """
#
# def parse_rows(s):
#   var_name = '\s*[a-zA-Z0-9_]+\s*'
#   quoted_var_name = "[\'\"]%s[\'\"]" % var_name
#   number = "\s*[0-9]+\s*"
#   regex = '(%s\[%s(?:\:%s)?\].*)' % (var_name, number, number)
#   matched = re.search(regex, s.strip())
#   if matched:
#     return matched.group(0)
#   return None
#
#
# def to_str(tree):
#   if len(tree.children) == 1 and not isinstance(tree.children[0], Tree):
#     return str(tree.children[0])
#   ret_str = ""
#   for child in tree.children:
#     if isinstance(child, Tree):
#       ret_str += to_str(child)
#     else:
#       ret_str += str(child)
#   return ret_str
#
#
# class DataframeVisitor(Visitor):
#   def __init__(self):
#     self.dfs = []
#
#   def expr(self, name):
#     # print(to_str(name))
#     self.dfs.append(to_str(name))
#
#
# def parse(s):
#   parser = Lark(GRAMMAR, keep_all_tokens=True)
#   tree = parser.parse(s)
#   # transformer = DataframeTransformer()
#   # transformer.transform(tree)
#   # print(tree)
#   visitor = DataframeVisitor()
#   visitor.visit(tree)
#   return visitor.dfs


class DataFrameParser(lib.O):
  def __init__(self):
    self.SPACE = ' '
    self.VAR_NAME = '%s*\w+%s*' % (self.SPACE, self.SPACE)
    self.CHAINED = '%s(?:\.%s)*' % (self.VAR_NAME, self.VAR_NAME)
    self.QUOTED_VAR_NAME = "%s*[\'\"]%s[\'\"]%s*" % (self.SPACE, self.CHAINED, self.SPACE)
    self.NUMBER = "%s*[0-9]+%s*" % (self.SPACE, self.SPACE)
    # self.ROW_REGEX = '(%s\[%s(?:\:%s)?\].*)' % (self.VAR_NAME, self.NUMBER, self.NUMBER)
    # self.COL_REGEX = '(%s\[(?:\[)?%s.*)' % (self.VAR_NAME, self.QUOTED_VAR_NAME)
    self.ROW_REGEX = '(%s\[%s(?:\:%s)?\].*)' % (self.CHAINED, self.NUMBER, self.NUMBER)
    self.COL_REGEX = '(%s\[(?:\[)?%s.*)' % (self.CHAINED, self.QUOTED_VAR_NAME)
    self.ATTR_REGEX, self.FUNC_REGEX = self.attr_and_func_regex()
    lib.O.__init__(self)

  def attr_and_func_regex(self):
    attrs, funcs = [], []
    method_type = type(pd.DataFrame.keys)
    for name, obj in inspect.getmembers(pd.DataFrame):
      if name[0] == "_":
        continue
      elif type(obj) == property:
        attrs.append(name)
      elif isinstance(obj, method_type):
        funcs.append(name)
    attr_str = "(?:%s)" % ("|".join(attrs))
    func_str = "(?:%s)" % ("|".join(funcs))
    # ATTR_REGEX = '(%s\.%s(?:\W.*|$))' % (self.VAR_NAME, attr_str)
    # FUNC_REGEX = '(%s\.%s\(.+)' % (self.VAR_NAME, func_str)
    ATTR_REGEX = '(%s\.%s(?:\W.*|$))' % (self.CHAINED, attr_str)
    FUNC_REGEX = '(%s\.%s\(.+)' % (self.CHAINED, func_str)
    return ATTR_REGEX, FUNC_REGEX

  def parse_rows(self, s):
    matched = re.search(self.ROW_REGEX, s.strip())
    matched_str = None if not matched else matched.group(0).strip()
    if matched_str and helper.is_bracket_balanced(matched_str):
      return matched_str
    return None

  def parse_cols(self, s):
    matched = re.search(self.COL_REGEX, s.strip())
    matched_str = None if not matched else matched.group(0).strip()
    if matched_str and helper.is_bracket_balanced(matched_str):
      return matched_str
    return None

  def parse_attr(self, s):
    matched = re.search(self.ATTR_REGEX, s.strip())
    matched_str = None if not matched else matched.group(0).strip()
    if matched_str and helper.is_bracket_balanced(matched_str):
      return matched_str
    return None

  def parse_func(self, s):
    matched = re.search(self.FUNC_REGEX, s.strip())
    matched_str = None if not matched else matched.group(0).strip()
    if matched_str and helper.is_bracket_balanced(matched_str):
      return matched_str
    return None

  def parse(self, s):
    def _update_matched(current, latest):
      if (not current) or (latest and len(latest) > len(current)):
        current = latest
      return current
    matched = _update_matched(None, self.parse_rows(s))
    matched = _update_matched(matched, self.parse_cols(s))
    matched = _update_matched(matched, self.parse_attr(s))
    matched = _update_matched(matched, self.parse_func(s))
    return matched

  def parse_file(self, file_path):
    stmts = []
    source = cache.read_file(file_path)
    for line in source.split("\n"):
      line = line.strip()
      if not line.startswith("#"):
        matched = self.parse(line)
        if matched:
          stmts.append(matched)
    return stmts


def _test_attr_regex():
  parser = DataFrameParser()
  attr_regex = parser.ATTR_REGEX
  x = "df.iloc = 5"
  match = re.search(attr_regex, x)
  if match:
    print(match.groups())
  else:
    print None


if __name__ == '__main__':
  _test_attr_regex()
