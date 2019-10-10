import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from lark import Lark, Visitor, Transformer, Tree

PD_GRAMMAR = """
  start: value (ASSIGNMENT_OPERATOR value)?
  binary_expr: value BINARY_OPERATOR value
  unary_expr: UNARY_OPERATOR value
  indexer: value ("." ("loc" | "iloc" | "ix" | "iy"))? "[" value "]"
  attribute: value "." value
  
  value: unary_expr
        | binary_expr
        | dict
        | array
        | tuple
        | slice_range
        | QUOTED_STRING
        | NUMBER
        | BOOL
        | NULL
        | NAME
        | lambda
        | func_call
        | attribute
        | indexer
        | values
        | if_else
  values: value? ("," value?)+
  array: "[" [value ("," value)*] "]"
  tuple: "(" [value ("," value)*] ")"
  dict: "{" [pair ("," pair)*] "}"
  pair: value ":" value
  slice_range: value? ":" value?
  // bracketed: "(" value ")"
  NULL: "None"
  BOOL: "True" | "False"
  lambda: "lambda" NAME ":" value
  if_else: value "if" value "else" value
  QUOTED_STRING : DOUBLE_QUOTED_STRING | SINGLE_QUOTED_STRING
  DOUBLE_QUOTED_STRING  : /"[^"]*"/
  SINGLE_QUOTED_STRING  : /'[^']*'/
  NAME: ("_"|LETTER) ("_"|LETTER|DIGIT)*
  ASSIGNMENT_OPERATOR: "="
                       | "+="
                       | "-="
                       | "*="
                       | "/="
                       | "**="
                       | "%="
                       | "//="
  BINARY_OPERATOR: "+" 
                   | "-"
                   | "**"
                   | "*"
                   | "//"
                   | "/"
                   | "%"
                   | "=="
                   | "!="
                   | ">="
                   | ">>"
                   | ">"
                   | "<="
                   | "<<"
                   | "<"
                   | "&"
                   | "|"
                   | "^"
                   | "and"
                   | "or"
                   | "is"
                   | "in"
  UNARY_OPERATOR: "not"
                  | "del"
                  | "~"
  
  func_name: NAME
  func_args: value ("," value)*
  func_kwarg: NAME "=" value
  func_kwargs: func_kwarg ("," func_kwarg)*
  args: (func_args | func_kwargs | (func_args "," func_kwargs))  
  func_call: (value ".")? func_name "(" args? ")"

  
  
  
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

  # print(parser.parse("df = df.groupby(['Title_cat'])['Age'].median().to_dict()"))
  # print(parser.parse("df.loc[(30 <= df['Age']), 'Age_cat']"))
  print(parser.parse("df.drop(['Ticket', 'Cabin'], axis=1)"))
  # print(parser.parse("df['Cabin'].apply(lambda x: 0 if pd.isnull(x) else 1)"))


def verify():
  from utils import cache
  misconceptions_path = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/src/main/python/misconceptions.xlsx"
  wb = cache.read_excel(misconceptions_path, read_only=True)
  # sheet = wb.get_sheet_by_name('HighSim-HighSyn')
  sheet = wb.get_sheet_by_name('LowSim-LowSyn')
  parser = pandas_parser()
  seen = set()
  for i, row in enumerate(sheet.iter_rows()):
    if i == 0:
      continue
    snippet = row[1].value
    if i >= 1 and snippet not in seen:
      print(i, snippet)
      seen.add(snippet)
      parser.parse(snippet)
    elif i % 100 == 0:
      print("Dont worry I'm running", i)


if __name__ == "__main__":
  verify()
  # _test()
