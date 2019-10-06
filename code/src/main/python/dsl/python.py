import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from lark import Lark, Visitor, Transformer, Tree

PD_GRAMMAR = """
  start: value (assignment_operator (value | values))?
  expr: value ( indexer | value | attribute)+
  //  expr: value+
  binary_expr: value binary_operator value
  unary_expr: unary_operator value
  indexer: ("." ("loc" | "iloc" | "ix" | "iy"))? "[" indexer_args "]"
  attribute: "." NAME
  
  value: dict
        | array
        | tuple
        | bracketed
        | slice_range
        | QUOTED_STRING
        | NUMBER
        | bool
        | null
        | NAME
        | lambda
        | func_call
        | array_access
        | if_else
        | expr
        | unary_expr
        | binary_expr
  values: [value ("," value)+]
  array: "[" [value ("," value)*] "]"
  tuple: "(" [value ("," value)+] ")"
  dict: "{" [pair ("," pair)*] "}"
  pair: value ":" value
  slice_range: value? ":" value?
  bracketed: "(" value ")"
  null: "None"
  bool: "True" | "False"
  lambda: "lambda" NAME ":" value
  if_else: value "if" value "else" value
  QUOTED_STRING : DOUBLE_QUOTED_STRING | SINGLE_QUOTED_STRING
  DOUBLE_QUOTED_STRING  : /"[^"]*"/
  SINGLE_QUOTED_STRING  : /'[^']*'/
  NAME: ("_"|LETTER) ("_"|LETTER|DIGIT)*
  assignment_operator: "="
                       | "+="
                       | "-="
                       | "*="
                       | "/="
                       | "**="
                       | "%="
                       | "//="
  binary_operator: "+" 
                   | "-"
                   | "*"
                   | "**"
                   | "/"
                   | "//"
                   | "%"
                   | "=="
                   | "!="
                   | ">"
                   | ">="
                   | "<"
                   | "<="
                   | "&"
                   | "|"
                   | "^"
                   | "<<"
                   | ">>"
                   | "and"
                   | "or"
                   | "is"
                   | "in"
  unary_operator: "not"
                  | "del"
                  | "~"
  
  func_name: NAME
  func_args: indexer_args ("," indexer_args)*
  func_kwarg: NAME "=" indexer_args
  func_kwargs: func_kwarg ("," func_kwarg)*
  args: (func_args | func_kwargs | (func_args "," func_kwargs))
  indexer_args: (value | values | func_name)
  func_call: "."? func_name "(" args? ")"
  
  array_access: value "[" indexer_args "]"
  
  
  
  // label: NUMBER | QUOTED_STRING
  // labels: label ("," label)+
  // label_array: "[" (label | labels)"]" 
  // slice_range: (label | expr)? ":" (label | expr)?
  // slice_ranges: slice_range_row "," slice_range_col
  // slice_range_row: ( label | expr | slice_range)
  // slice_range_col: ( label | expr | slice_range)
  // exprs: expr ("," expr)+
  // exprs_array: "[" (expr | exprs)"]"
  // bools: bool ("," bool)+
  // bool_array: "[" (bool | bools)"]"
  // indexer_args: (label | labels | label_array | slice_range | slice_ranges | bool | bools | bool_array | expr | exprs | exprs_array | func_name)
  // loc: "." "loc" "[" indexer_args "]"
  // iloc: "." "iloc" "[" indexer_args "]"
  // accessor: "[" indexer_args "]"
  
  // %import common.CNAME -> NAME
  %import common.LETTER -> LETTER
  %import common.DIGIT -> DIGIT
  %import common.SIGNED_NUMBER -> NUMBER
  %import common.WORD
  %import common.WS
  %import common.NEWLINE -> NEWLINE
  %ignore WS
"""


def pandas_parser():
  return Lark(PD_GRAMMAR)


def _test():
  parser = pandas_parser()
  # print(parser.parse("df.iloc[1:2, df[[2]]]"))
  # print(parser.parse("df.set_value(axis=8.05)"))
  print(parser.parse("df = df.groupby(['Title_cat'])['Age'].median().to_dict()"))


def verify():
  from utils import cache
  misconceptions_path = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/src/main/python/misconceptions.xlsx"
  wb = cache.read_excel(misconceptions_path, read_only=True)
  sheet = wb.get_sheet_by_name('HighSim-HighSyn')
  parser = pandas_parser()
  for i, row in enumerate(sheet.iter_rows()):
    if i == 0:
      continue
    if i >= 1:
      print(i, row[1].value)
      parser.parse(row[1].value)


if __name__ == "__main__":
  verify()
  # _test()
