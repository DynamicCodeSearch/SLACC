import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import astor

from utils.lib import O


class Statement(O):
  def __init__(self, **kwargs):
    self.file_source = None
    self.method_name = None
    self.start_pos = None
    self.end_pos = None
    self._ast = None
    self.is_return = False
    O.__init__(self, **kwargs)

  def get_ast(self):
    return self._ast

  def get_text(self):
    return astor.to_source(self._ast).strip("\n")

  def pprint(self):
    print(self.get_text())


class GroupedStatement(Statement):
  def __init__(self, **kwargs):
    self.statements = []
    Statement.__init__(self, **kwargs)


class ChoiceGroupedStatement(Statement):
  def __init__(self, **kwargs):
    self.choices = [] # [[Statements], [Statements]]
    Statement.__init__(self, **kwargs)

#
def _test():
  import asttokens
  code = """
from .dummy import *



def func_46bf254f3cab42aaa0e33b88f9d22ec5(dic, y, z, x, lst):
  def local(d):
    d += 2
    return d ** 2
  global c
  a = 5
  b = 10
  if a > 10:
    b += 1
  elif a > 20:
    b += 2
    c = c + 1
  elif a > 30:
    b += 3
    c = c + 2
  else:
    b += 4
    c = c + 3
    c += 8
  for i in range(4):
    a *= 2
    b += 1
    lst.append(a + b)
    dic[a] = a + b + sum(tup)
  return a + b + c * y ** z * local(x)
  """
  import ast
  tree = ast.parse(code)
  print(ast.dump(tree))
  # ast_tokenized = asttokens.ASTTokens(code, parse=True)
  # print(ast_tokenized.get_text(ast_tokenized.tree))
#
#
if __name__ == "__main__":
  _test()
