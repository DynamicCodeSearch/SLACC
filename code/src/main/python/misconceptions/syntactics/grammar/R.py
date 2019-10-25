import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from lark import Lark

R_GRAMMAR = """
  start: value (ASSIGNMENT_OPERATOR value)?
  // expr: value ( indexer | value | attribute)+
  binary_expr: value BINARY_OPERATOR value
  unary_expr: UNARY_OPERATOR value
  indexer: value "[" value "]"
  attribute: value "$" value
  
  value: unary_expr
        | binary_expr
        | array
        | list
        | matrix
        | data_frame
        | tuple
        | slice_range
        | QUOTED_STRING
        | NUMBER
        | BOOL
        | NULL
        | NAME
        | if_else
        | func_call
        | attribute
        | indexer
        | values
  values: value? ("," value?)+
  array: ("c" "(" [value ("," value)*] ")") | ("[" value? ("," value?)* "]")
  list: "list" "(" [value ("," value)*] ")"
  matrix: "matrix" "(" args ")"
  data_frame: "data.frame" "(" args ")"
  tuple: "(" [value ("," value)*] ")"
  QUOTED_STRING : DOUBLE_QUOTED_STRING | SINGLE_QUOTED_STRING | TILDE_QUOTED_STRING
  DOUBLE_QUOTED_STRING  : /"[^"]*"/
  SINGLE_QUOTED_STRING  : /'[^']*'/
  TILDE_QUOTED_STRING   : /`[^']*`/
  NAME: ("_"|LETTER) ("_"|LETTER|DIGIT|".")*
  BOOL: "TRUE" | "FALSE"
  if_else: "ifelse" "(" value "," value "," value")"
  slice_range: value? ":" value?
  NULL: "NULL" | "NaN"
  ASSIGNMENT_OPERATOR: "="
                       | "<-"
  BINARY_OPERATOR: "+" 
                   | "-"
                   | "**"
                   | "*"
                   | "/"
                   | "^"
                   | "%%"
                   | "%/%"
                   | ">="
                   | ">"
                   | "<="
                   | "<"
                   | "=="
                   | "!="
                   | "|"
                   | "&"
  UNARY_OPERATOR: "!"
                  | "-"
  
  func_name: NAME | TILDE_QUOTED_STRING
  func_args: value ("," value)*
  func_kwarg: NAME "=" value
  func_kwargs: func_kwarg ("," func_kwarg)*
  args: (func_args | func_kwargs | (func_args "," func_kwargs))
  //indexer_args: (value | values | func_name)
  func_call: func_name "(" args? ")"
  
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
  # print(parser.parse('table(df$Parch, df$Survived)'))
  print(parser.parse('mean(df$Fare)'))



def verify():
  from utils import cache
  misconceptions_path = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/src/main/python/misconceptions.xlsx"
  wb = cache.read_excel(misconceptions_path, read_only=True)
  # sheet = wb.get_sheet_by_name('HighSim-HighSyn')
  sheet = wb.get_sheet_by_name('LowSim-LowSyn')
  parser = r_parser()
  seen = set()
  for i, row in enumerate(sheet.iter_rows()):
    if i == 0:
      continue
    snippet = row[0].value
    if i >= 1 and snippet not in seen:
      print(i, snippet)
      seen.add(snippet)
      parser.parse(snippet)
    elif i % 100 == 0:
      print("Dont worry I'm running", i)


if __name__ == "__main__":
  # verify()
  _test()