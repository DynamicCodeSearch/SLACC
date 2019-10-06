import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from lark import Lark

R_GRAMMAR = """
  start: value (assignment_operator (value | values))?
  expr: value ( indexer | value | attribute)+
  binary_expr: value binary_operator value
  unary_expr: unary_operator value
  indexer: ("." ("loc" | "iloc" | "ix" | "iy"))? "[" indexer_args "]"
  attribute: "$" NAME
  
  value: array
        | list
        | matrix
        | data_frame
        | bracketed
        | slice_range
        | QUOTED_STRING
        | NUMBER
        | bool
        | null
        | NAME
        | if_else
        | "-" value
        | "(" ")"
        | func_call
        | expr
        | unary_expr
        | binary_expr
  values: [value? ("," value?)+]
  array.2: "c" "(" [value ("," value)*] ")"
  list.2: "list" "(" [value ("," value)*] ")"
  matrix.2: "matrix" "(" args ")"
  data_frame.2: "data.frame" "(" args ")"
  bracketed: "(" value ")"
  QUOTED_STRING : DOUBLE_QUOTED_STRING | SINGLE_QUOTED_STRING
  DOUBLE_QUOTED_STRING  : /"[^"]*"/
  SINGLE_QUOTED_STRING  : /'[^']*'/
  NAME: ("_"|LETTER) ("_"|LETTER|DIGIT|".")*
  bool: "TRUE" | "FALSE"
  if_else.2: "ifelse" "(" value "," value "," value")"
  slice_range: value? ":" value?
  null: "NULL" | "NaN"
  assignment_operator: "="
                       | "<-"
  binary_operator: "+" 
                   | "-"
                   | "*"
                   | "**"
                   | "/"
                   | "^"
                   | "**"
                   | "%%"
                   | "%/%"
                   | ">"
                   | ">="
                   | "<"
                   | "<="
                   | "=="
                   | "!="
                   | "|"
                   | "&"
  unary_operator: "!"
  
  func_name: NAME
  func_args: indexer_args ("," indexer_args)*
  func_kwarg: NAME "=" indexer_args
  func_kwargs: func_kwarg ("," func_kwarg)*
  args: (func_args | func_kwargs | (func_args "," func_kwargs))
  indexer_args: (value | values | func_name)
  func_call: "."? func_name "(" args? ")"
  
  // %import common.CNAME -> NAME
  %import common.SIGNED_NUMBER -> NUMBER
  %import common.LETTER -> LETTER
  %import common.DIGIT -> DIGIT
  %import common.WORD
  %import common.WS
  %import common.NEWLINE -> NEWLINE
  %ignore WS
"""


def r_parser():
  return Lark(R_GRAMMAR)


def _test():
  parser = r_parser()
  # print(parser.parse("df.iloc[1:2, df[[2]]]"))
  # print(parser.parse("df.set_value(dfaxis=8.05)"))
  print(parser.parse('table(df$Parch, df$Survived)'))


def verify():
  from utils import cache
  misconceptions_path = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/src/main/python/misconceptions.xlsx"
  wb = cache.read_excel(misconceptions_path, read_only=True)
  sheet = wb.get_sheet_by_name('HighSim-HighSyn')
  parser = r_parser()
  for i, row in enumerate(sheet.iter_rows()):
    if i == 0:
      continue
    if i >= 1:
      print(i, row[0].value)
      parser.parse(row[0].value)


if __name__ == "__main__":
  # verify()
  _test()