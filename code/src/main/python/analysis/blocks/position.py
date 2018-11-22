import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from utils.lib import O


class Position(O):
  def __init__(self, line, col_offset, **kwargs):
    self.line = line
    self.col_offset = col_offset
    O.__init__(self, **kwargs)

  def __eq__(self, other):
    if self is other:
      return True
    elif type(self) != type(other):
      return False
    else:
      return self.line == other.line and self.col_offset == other.col_offset

  def __lt__(self, other):
    if self.line < other.line:
      return True
    elif self.line == other.line:
      return self.col_offset < other.col_offset
    return False

  def __gt__(self, other):
    if self.line > other.line:
      return True
    elif self.line == other.line:
      return self.col_offset > other.col_offset
    return False

  def __cmp__(self, other):
    if self < other:
      return -1
    elif self > other:
      return 1
    else:
      return 0

  def __hash__(self):
    return hash("$$".join(map(str, ["dict", self.line, self.col_offset])))

  def __repr__(self):
    return "pos:(%d, %d)" % (self.line, self.col_offset)

  def to_bson(self):
    return self.__dict__

  @staticmethod
  def from_bson(bson_dict):
    return Position(bson_dict['line'], bson_dict['col_offset'])

  @staticmethod
  def get_position(node):
    return Position(node.lineno, node.col_offset)
