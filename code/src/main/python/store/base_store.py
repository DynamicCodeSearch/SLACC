import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from utils.lib import O


class FunctionStore(O):
  def __init__(self, dataset, **kwargs):
    O.__init__(self, **kwargs)
    self.dataset = dataset

  def load_functions(self):
    raise NotImplementedError("Should be implemented in subclass")

  @staticmethod
  def __is_object_return(metadata):
    """
    Is the return type of object
    :param metadata:
    :return:
    """
    return not metadata["isArray"] and not metadata["isPrimitive"]

  @staticmethod
  def __get_return_vals(returns):
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
