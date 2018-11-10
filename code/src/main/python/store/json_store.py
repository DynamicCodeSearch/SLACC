import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import re

from store import base_store
from utils import lib, logger, cache
from sos.function import Function, Outputs

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


class FunctionStore(base_store.FunctionStore):
  def __init__(self, dataset, **kwargs):
    base_store.FunctionStore.__init__(self, dataset, **kwargs)

  def load_functions(self):
    functions = []
    results_folder = lib.get_dataset_functions_results_folder(self.dataset)
    for json_file in lib.list_files(results_folder, check_nest=True, is_absolute=True):
      if not json_file.endswith(".json"):
        continue
      functions += self.__load_functions_for_class(json_file)
    valid_functions = [func for func in functions if func.is_useful()]
    LOGGER.info("Valid Functions : %d / %d" % (len(valid_functions), len(functions)))
    return valid_functions

  def __load_functions_for_class(self, class_json_file):
    """
    Load functions for class json file.
    :param class_json_file: Json file containing the results for the class json.
    :return: Parsed functions from class json file.
    """
    def get_package(json_file):
      return json_file.split("%sfunctions%s" %
                             (os.path.sep, os.path.sep))[-1].rsplit(os.path.sep, 1)[0].replace(os.path.sep, ".")

    class_json = cache.load_json(class_json_file)
    class_name = cache.get_file_name(class_json_file)
    package = get_package(class_json_file)
    functions = []
    function_pattern = re.compile(r'^func_')
    class_metadata = self.__load_class_metadata(package, class_name)
    for function_name, details in class_json.items():
      if not function_pattern.match(function_name):
        continue
      function_metadata = class_metadata[function_name]
      return_meta_data = function_metadata["return"]
      outputs = Outputs(details["outputs"])
      funct = Function(name=function_name, dataset=self.dataset,
                       class_name=class_name, package=package,
                       input_key=details["inputKey"], outputs=outputs,
                       lines_touched=function_metadata.get("linesTouched", None),
                       span=function_metadata.get("span", None), body=function_metadata["body"])
      if FunctionStore.__is_object_return(return_meta_data):
        for attribute, returns in FunctionStore.__get_return_vals(outputs.returns).items():
          clone = funct.clone()
          clone.outputs = outputs.clone()
          clone.outputs.returns = returns[:]
          clone.return_attribute = attribute
          # clone.is_useful()
          functions.append(clone)
      else:
        # funct.is_useful()
        functions.append(funct)
    return functions

  def __load_class_metadata(self, package, class_name):
    metadata_file = os.path.join(lib.get_dataset_meta_results_folder(self.dataset), package.replace(".", os.path.sep),
                                 "%s.json" % class_name)
    return cache.load_json(metadata_file)



