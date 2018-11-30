import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from store import base_store
from utils import lib, logger, cache
import properties

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


class InputStore(base_store.InputStore):
  def __init__(self, dataset, **kwargs):
    base_store.InputStore.__init__(self, dataset, **kwargs)

  def load_inputs(self, args_key):
    args_index = cache.load_json(lib.get_dataset_arg_index(self.dataset))
    if args_key not in args_index:
      return None
    arg_files_name = os.path.join(lib.get_dataset_args_folder(self.dataset), "%s.json" % args_index[args_key])
    arguments = cache.load_json(arg_files_name)
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
    self.class_meta_data = {}

  def load_function(self, function_name):
    raise NotImplementedError("Not Implemented for JSON")

  def load_functions(self):
    functions = []
    results_folder = lib.get_dataset_functions_results_folder(self.dataset)
    for json_file in cache.list_files(results_folder, check_nest=True, is_absolute=True):
      if not json_file.endswith(".json"):
        continue
      functions += self.__load_functions_for_class(json_file)
    return functions

  def __load_functions_for_class(self, class_json_file):
    """
    Load functions for class json file.
    :param class_json_file: Json file containing the results for the class json.
    :return: Parsed functions from class json file.
    """
    class_json = cache.load_json(class_json_file)
    return class_json.values()

  def load_metadata(self, funct):
    return self.__load_class_metadata(funct["package"], funct["class"])[funct["name"]]

  def __load_class_metadata(self, package, class_name):
    metadata_file = os.path.join(lib.get_dataset_meta_results_folder(self.dataset), package.replace(".", os.path.sep),
                                 "%s.json" % class_name)
    if metadata_file not in self.class_meta_data:
      self.class_meta_data[metadata_file] = cache.load_json(metadata_file)
    return self.class_meta_data[metadata_file]

  def update_function_arg_type(self, function_name, function_arg_types):
    raise NotImplementedError("Not Implemented for JSON")

  def load_function_arg_type(self, function_name):
    raise NotImplementedError("Not Implemented for JSON")

  def save_py_function(self, function_json):
    raise NotImplementedError("Not Implemented for JSON")

  def load_py_function(self, function_name):
    raise NotImplementedError("Not Implemented for JSON")

  def exists_py_function(self, function_json):
    raise NotImplementedError("Not Implemented for JSON")

  def save_failed_py_function(self, function_json):
    raise NotImplementedError("Not Implemented for JSON")

  def is_invalid_py_function(self, function_name):
    raise NotImplementedError("Not Implemented for JSON")

  def load_py_functions(self):
    raise NotImplementedError("Not Implemented for JSON")

  def save_py_metadata(self, func_json):
    raise NotImplementedError("Not Implemented for JSON")

  def load_py_metadata(self, function_name):
    raise NotImplementedError("Not Implemented for JSON")
