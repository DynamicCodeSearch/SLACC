import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


from analysis.helpers import constants as a_consts
from utils.lib import O


class BasicType(O):
  def __init__(self, **kwargs):
    self.name = None
    self.is_primitive_type = None
    self.module = None  # Set only for non primitives
    self.is_valid = True
    O.__init__(self, **kwargs)

  @staticmethod
  def get_name(value):
    return type(value).__name__

  @staticmethod
  def get_module(value):
    return type(value).__module__

  def __hash__(self):
    return hash("$$".join(map(str, [self.name, self.is_primitive_type, self.module, self.is_valid])))

  def __eq__(self, other):
    if other is None or not isinstance(other, BasicType):
      return False
    return hash(self) == hash(other)

  @staticmethod
  def get_type(value):
    var_type = BasicType()
    var_type.name = BasicType.get_name(value)
    var_type.is_primitive = BasicType.is_primitive(var_type.name)
    if not var_type.is_primitive:
      var_type.module = BasicType.get_module(value)
    return var_type

  @staticmethod
  def is_primitive(type_name):
    return type_name in a_consts.PRIMITIVES

  @staticmethod
  def is_none(value):
    return value is None

  def to_bson(self):
    return {
      "name": self.name,
      "is_primitive_type": self.is_primitive_type,
      "module": self.module,
      "is_valid": self.is_valid
    }

  @staticmethod
  def from_json(bson_dict):
    o = BasicType()
    o.name = str(bson_dict['name'])
    o.is_primitive_type = bson_dict['is_primitive_type']
    if "module" in bson_dict:
      o.module = str(bson_dict['module'])
    o.is_valid = bson_dict['is_valid']
    return o


class ListType(O):
  def __init__(self, **kwargs):
    self.name = "list"
    self.is_list = True
    self.is_valid = True
    self.type = None
    O.__init__(self, **kwargs)

  def to_bson(self):
    return {
      "name": self.name,
      "is_list": self.is_list,
      "is_valid": self.is_valid,
      "type": self.type.to_bson() if self.type else None
    }

  def __hash__(self):
    return hash("$$".join(map(str, ["list", self.is_list, self.is_valid, self.type])))

  def __eq__(self, other):
    if other is None or not isinstance(other, ListType):
      return False
    return hash(self) == hash(other)

  @staticmethod
  def get_type(value):
    var_type = ListType()
    ind_types = ListType.get_each_types(value)
    if len(ind_types) == 1:
      var_type.type = ind_types.pop()
    else:
      var_type.is_valid = False
    return var_type

  @staticmethod
  def get_each_types(value):
    types = set()
    for v_i in value:
      if v_i is not None:
        types.add(get_type(v_i))
    return types

  def to_bson(self):
    return {
      "name": self.name,
      "is_list": self.is_list,
      "is_valid": self.is_valid,
      "type": self.type.to_bson() if self.type else None
    }

  @staticmethod
  def from_json(bson_dict):
    o = ListType()
    o.name = str(bson_dict['name'])
    o.is_list = bson_dict['is_list']
    o.is_valid = bson_dict['is_valid']
    o.type = from_bson(bson_dict['type']) if 'type' in bson_dict else None
    return o


class DictType(O):
  def __init__(self, **kwargs):
    O.__init__(self, **kwargs)
    self.name = "dict"
    self.is_valid = True
    self.is_dict = True
    self.key_type = None
    self.val_type = None

  def __hash__(self):
    return hash("$$".join(map(str, ["dict", self.is_valid, self.is_dict, self.key_type, self.val_type])))

  def __eq__(self, other):
    if other is None or not isinstance(other, DictType):
      return False
    return hash(self) == hash(other)

  @staticmethod
  def get_type(value):
    var_type = DictType()
    key_types = ListType.get_each_types(value.keys())
    val_types = ListType.get_each_types(value.values())
    if len(key_types) == 1 and len(val_types) == 1:
      var_type.key_type = key_types.pop()
      var_type.val_type = val_types.pop()
    else:
      var_type.is_valid = False
    return var_type

  def to_bson(self):
    return {
      "name": self.name,
      "is_dict": self.is_dict,
      "is_valid": self.is_valid,
      "key_type": self.key_type.to_bson() if self.key_type else None,
      "val_type": self.val_type.to_bson() if self.val_type else None
    }

  @staticmethod
  def from_json(bson_dict):
    o = DictType()
    o.name = str(bson_dict['name'])
    o.is_dict = bson_dict['is_dict']
    o.is_valid = bson_dict['is_valid']
    o.key_type = from_bson(bson_dict['key_type']) if 'key_type' in bson_dict else None
    o.val_type = from_bson(bson_dict['val_type']) if 'val_type' in bson_dict else None
    return o


class TupleType(O):
  def __init__(self, **kwargs):
    O.__init__(self, **kwargs)
    self.name = "tuple"
    self.is_valid = True
    self.is_tuple = True
    self.types = []

  def to_bson(self):
    return {
      "name": self.name,
      "is_tuple": self.is_tuple,
      "is_valid": self.is_valid,
      "types": [t.to_bson() for t in self.types] if self.types else None
    }

  def __hash__(self):
    return hash("$$".join(map(str, ["tuple", self.is_valid, self.is_tuple, "$$".join(map(str, self.types))])))

  def __eq__(self, other):
    if other is None or not isinstance(other, TupleType):
      return False
    return hash(self) == hash(other)

  @staticmethod
  def get_type(value):
    var_type = TupleType()
    for v_0 in value:
      var_type.types.append(get_type(v_0))
    return var_type

  @staticmethod
  def from_json(bson_dict):
    o = TupleType()
    o.name = str(bson_dict['name'])
    o.is_tuple = bson_dict['is_tuple']
    o.is_valid = bson_dict['is_valid']
    o.types = [from_bson(t) for t in bson_dict['types']] if 'types' in bson_dict else None
    return o


def get_type(value):
  if BasicType.get_name(value) == "list":
    return ListType.get_type(value)
  elif BasicType.get_name(value) == "dict":
    return DictType.get_type(value)
  elif BasicType.get_name(value) == "tuple":
    return TupleType.get_type(value)
  else:
    return BasicType.get_type(value)


def from_bson(bson_dict):
  if bson_dict is None:
    return None
  elif bson_dict.get("is_list", None):
    return ListType.from_json(bson_dict)
  elif bson_dict.get("is_dict", None):
    return DictType.from_json(bson_dict)
  elif bson_dict.get("is_tuple", None):
    return TupleType.from_json(bson_dict)
  else:
    return BasicType.from_json(bson_dict)


def is_valid_type(value):
  return BasicType.get_name(value) != "tuple"
