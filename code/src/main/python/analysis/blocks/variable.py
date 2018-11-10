import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


from utils.lib import O


class Variable(O):
  def __init__(self, name, scope, var_type, positions, **kwargs):
    self.name = name
    self.scope = scope
    self.var_type = var_type
    self.positions = positions
    O.__init__(self, **kwargs)
