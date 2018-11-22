import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from utils.lib import O


class InputStore(O):
  def __init__(self, dataset, **kwargs):
    O.__init__(self, **kwargs)
    self.dataset = dataset

  def load_inputs(self, args_key):
    raise NotImplementedError("Should be implemented in subclass")

  @staticmethod
  def is_array(arg_sets):
    if not type(arg_sets[0]) is list:
      return False
    return len(arg_sets[0]) != len(arg_sets[1]) != len(arg_sets[2])


class FunctionStore(O):
  def __init__(self, dataset, **kwargs):
    O.__init__(self, **kwargs)
    self.dataset = dataset

  def load_functions(self):
    raise NotImplementedError("Should be implemented in subclass")

  def load_metadata(self, funct):
    raise NotImplementedError("Should be implemented in subclass")

  def update_function_arg_type(self, function_name, function_arg_types):
    raise NotImplementedError("Should be implemented in subclass")

  @staticmethod
  def is_object_return(metadata):
    """
    Is the return type of object
    :param metadata:
    :return:
    """
    return not metadata["isArray"] and not metadata["isPrimitive"]

  @staticmethod
  def get_return_vals(returns):
    return_keys = []

    def get_key(d):
      keys = []
      for k in d.keys():
        if isinstance(d[k], dict):
          keys += ["%s.%s" % (k, k_i) for k_i in get_key(d[k])]
        else:
          keys.append(k)
      return keys

    def get_value(d):
      values = []
      for k in d.keys():
        if isinstance(d[k], dict):
          values += get_value(d[k])
        else:
          values.append(d[k])
      return values

    for ret in returns:
      if ret is None: continue
      return_keys = get_key(ret)
      break
    ret_vals_dict = {k: [] for k in return_keys}
    for ret in returns:
      if ret is None:
        for k in return_keys:
          ret_vals_dict[k].append(None)
      else:
        for k, v in zip(return_keys, get_value(ret)):
          ret_vals_dict[k].append(v)
    return ret_vals_dict


class PyFileMetaStore(O):
  def __init__(self, dataset, **kwargs):
    O.__init__(self, **kwargs)
    self.dataset = dataset

  def load_meta(self, file_name):
    raise NotImplementedError("Should be implemented in subclass")

  def save_meta(self, bson_dict):
    raise NotImplementedError("Should be implemented in subclass")