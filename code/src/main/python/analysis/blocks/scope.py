import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


from analysis import constants as a_consts
from utils.lib import O


class Scope(O):
  def __init__(self, name, parent, **kwargs):
    self.name = name
    self.parent = parent
    O.__init__(self, **kwargs)

  def __str__(self):
    as_str = self.name
    if self.parent:
      as_str = "%s%s%s" % (str(self.parent), a_consts.SCOPE_SEPARATOR, as_str)
    return as_str

  def __repr__(self):
    return self.__str__()

  def __hash__(self):
    return hash(str(self))

  def __eq__(self, other):
    if other is None or not isinstance(other, BasicType):
      return False
    return hash(self) == hash(other)
