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

  @staticmethod
  def get_position(node):
    return Position(node.lineno, node.col_offset)