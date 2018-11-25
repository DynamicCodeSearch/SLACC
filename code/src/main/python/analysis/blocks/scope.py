import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


from analysis.helpers import constants as a_consts
from utils.lib import O


class Scope(O):
  def __init__(self, name, parent, **kwargs):
    self.name = name
    self.parent = parent
    self.children = {}
    self._danglings = {}
    O.__init__(self, **kwargs)

  def get_danglings(self):
    return self._danglings

  def update_dangling(self, name, position):
    if name in self._danglings:
      positions = self._danglings.get(name, set())
      positions.add(position)
    else:
      positions = {position}
    self._danglings[name] = positions

  def set_danglings(self, danglings):
    self._danglings = danglings

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
    if other is None or not isinstance(other, Scope):
      return False
    return hash(self) == hash(other)

  def to_bson(self):
    d = {"name": self.name}
    if self.parent:
      d['parent'] = str(self.parent)
    if self.children:
      d['children'] = {}
      for name, child in self.children.items():
        d['children'][name] = str(child)
    return d


def from_bson(scope_map):
  scopes = {}
  for key, val in scope_map.items():
    scope = Scope(val['name'], val.get('parent', None))
    scope.children = val.get('children', None)
    scopes[key] = scope
  for key, scope in scopes.items():
    if scope.parent:
      scope.parent = scopes[scope.parent]
    if scope.children:
      for child_key, child_str in scope.children.items():
        scope.children[child_key] = scopes[child_str]
  return scopes
