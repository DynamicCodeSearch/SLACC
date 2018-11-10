import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


from store import base_store, mongo_driver
from utils import logger
import properties

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


class InputStore(base_store.InputStore):
  def __init__(self, dataset, **kwargs):
    base_store.InputStore.__init__(self, dataset, **kwargs)

  def load_inputs(self, args_key):
    arguments = mongo_driver.get_collection(self.dataset, "fuzzed_args").find_one({"key": args_key})["args"]
    assert len(arguments) == properties.FUZZ_ARGUMENT_SIZE
    if self.is_array(arguments):
      key_args = arguments
    else:
      key_args = [[] for _ in range(len(arguments[0]))]
      for i in range(len(arguments[0])):
        for arg in arguments:
          key_args[i].append(arg)
    return key_args


class FunctionStore(base_store.FunctionStore):
  def __init__(self, dataset, **kwargs):
    base_store.FunctionStore.__init__(self, dataset, **kwargs)

  def load_functions(self):
    collection = mongo_driver.get_collection(self.dataset, "functions_executed")
    return collection.find()

  def load_metadata(self, funct):
    return mongo_driver.get_collection(self.dataset, "functions_metadata").find_one({"name": funct["name"]})
