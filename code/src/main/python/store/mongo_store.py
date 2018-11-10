import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


import re


from store import base_store, mongo_driver
from utils import logger
from sos.function import Function, Outputs

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


class FunctionStore(base_store.FunctionStore):
  def __init__(self, dataset, **kwargs):
    base_store.FunctionStore.__init__(self, dataset, **kwargs)

  def load_functions(self):
    functions = []
    collection = mongo_driver.get_collection(self.dataset, "functions_executed")
    function_pattern = re.compile(r'^func_')
    for func_bson in collection.find():
      if not function_pattern.match(func_bson['name']): continue
      meta_data = self.load_metadata(func_bson['name'])
      return_meta_data = meta_data["return"]
      outputs = Outputs(func_bson["outputs"])
      funct = Function(name=func_bson["name"], dataset=self.dataset,
                       class_name=func_bson["class"], package=func_bson["package"],
                       input_key=func_bson["inputKey"], outputs=outputs,
                       lines_touched=meta_data.get("linesTouched", None),
                       span=meta_data.get("span", None), body=meta_data["body"])
      if FunctionStore.__is_object_return(return_meta_data):
        for attribute, returns in FunctionStore.__get_return_vals(outputs.returns).items():
          clone = funct.clone()
          clone.outputs = outputs.clone()
          clone.outputs.returns = returns[:]
          clone.return_attribute = attribute
          functions.append(clone)
      else:
        functions.append(funct)
    valid_functions = [func for func in functions if func.is_useful()]
    LOGGER.info("Valid Functions : %d / %d" % (len(valid_functions), len(functions)))
    return valid_functions

  def load_metadata(self, name):
    return mongo_driver.get_collection(self.dataset, "functions_metadata").find_one({"name": name})
