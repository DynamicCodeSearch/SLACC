import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


from analysis.helpers import constants as a_consts
from analysis.blocks import types as types_block
from analysis.blocks import position as position_block
from utils.lib import O


class Variable(O):
  def __init__(self, name, scope, var_type, positions, **kwargs):
    self.name = name
    self.scope = scope
    self.var_type = var_type
    self.positions = positions
    self.type = None
    self._store_positions = set()
    self._updated_positions = set()
    self._prev_value = None
    self._is_type_set = False
    O.__init__(self, **kwargs)

  def to_bson(self):
    d = {
      "name": self.name,
      "scope": str(self.scope),
      "var_type": self.var_type,
      "positions": [],
      "type": None,
      "_store_positions": [],
      "_updated_positions": []
    }
    if self.type:
      d['type'] = self.type.to_bson()
    if self.positions:
      for position in self.positions:
        d['positions'].append(position.to_bson())
    if self._store_positions:
      for position in self._store_positions:
        d['_store_positions'].append(position.to_bson())
    if self._updated_positions:
      for position in self._updated_positions:
        d['_updated_positions'].append(position.to_bson())
    return d

  @staticmethod
  def from_json(bson_dict, scope):
    positions = [position_block.Position.from_bson(pos) for pos in bson_dict['positions']]
    variable = Variable(str(bson_dict['name']), scope, str(bson_dict['var_type']), positions)
    if "type" in bson_dict:
      variable.type = types_block.from_bson(bson_dict['type'])
    if "_store_positions" in bson_dict:
      variable._store_positions = set([position_block.Position.from_bson(p) for p in bson_dict['_store_positions']])
    if "_updated_positions" in bson_dict:
      variable._updated_positions = set([position_block.Position.from_bson(p) for p in bson_dict['_updated_positions']])
    return variable

  def is_type_set(self):
    return self._is_type_set

  def get_prev_value(self):
    return self._prev_value

  def set_prev_value(self, prev_value):
    self._prev_value = prev_value

  def update_store_position(self, position):
    self._store_positions.add(position)

  def get_store_positions(self):
    return self._store_positions

  def update_updated_position(self, position):
    self._updated_positions.add(position)

  def get_updated_positions(self):
    return self._updated_positions

  def get_position_by_line(self, line_no):
    for position in self.positions:
      if position.line == line_no:
        return position
    return None

  def is_updated_in_range(self, start, end):
    for position in sorted(self.get_updated_positions()):
      if start <= position <= end:
        return True
    return False

  def is_argument(self, start, local_variables, line_numbers):
    if self.var_type == a_consts.VAR_TYPE.ARG:
      return True
    if self not in local_variables and not isinstance(self.type, types_block.BasicType):
      return True
    updated_positions = set()
    for pos in self.get_updated_positions():
      if pos.line in line_numbers:
        updated_positions.add(pos)
    return len(updated_positions) == 0 or sorted(updated_positions)[0] < start

  def has_visited(self, position):
    return position in self.get_updated_positions()
