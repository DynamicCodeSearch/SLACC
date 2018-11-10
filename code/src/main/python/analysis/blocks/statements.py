import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


from utils.lib import O


class Statement(O):
  def __init__(self, **kwargs):
    self.file_source = None
    self.method_name = None
    self.start_pos = None
    self.end_pos = None
    self.ast = None
    O.__init__(self, **kwargs)


class GroupedStatement(Statement):
  def __init__(self, **kwargs):
    self.statements = []
    O.__init__(self, **kwargs)


class ChoiceGroupedStatement(Statement):
  def __init__(self, **kwargs):
    self.choices = [] # [[Statements], [Statements]]
    O.__init__(self, **kwargs)
