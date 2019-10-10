import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


from store import base_store, mongo_driver
from utils import logger, lib
import properties
import re

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
    self.is_test = None
    base_store.FunctionStore.__init__(self, dataset, **kwargs)

  def load_function(self, function_name):
    collection_name = "test_functions_executed" if self.is_test else "functions_executed"
    collection = mongo_driver.get_collection(self.dataset, collection_name)
    return collection.find_one({"name": function_name})

  def load_functions(self):
    collection_name = "test_functions_executed" if self.is_test else "functions_executed"
    collection = mongo_driver.get_collection(self.dataset, collection_name)
    return collection.find()

  def load_metadata(self, funct):
    return mongo_driver.get_collection(self.dataset, "functions_metadata").find_one({"name": funct["name"]})

  def update_function_arg_type(self, function_name, function_arg_types):
    collection = mongo_driver.get_collection(self.dataset, "py_functions_arg_types")
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "name")
    collection.insert({
      "name": function_name,
      "types": function_arg_types
    })

  def load_function_arg_type(self, function_name):
    try:
      return mongo_driver.get_collection(self.dataset, "py_functions_arg_types").find_one({"name": function_name})
    except Exception as e:
      LOGGER.critical("Failed to load args for function: '%s'. Returning None."
                      "\nMessage: %s" % (function_name, e.message))
      return None

  def save_py_function(self, function_json):
    collection_name = "test_py_functions_executed" if self.is_test else "py_functions_executed"
    collection = mongo_driver.get_collection(self.dataset, collection_name)
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "name")
    try:
      collection.insert(function_json)
    except Exception:
      del function_json['outputs']
      self.save_failed_py_function(function_json)

  def load_py_function(self, function_name):
    collection_name = "test_py_functions_executed" if self.is_test else "py_functions_executed"
    collection = mongo_driver.get_collection(self.dataset, collection_name)
    return collection.find_one({"name": function_name})

  def exists_py_function(self, function_name):
    return self.load_py_function(function_name) is not None

  def save_failed_py_function(self, function_json):
    collection_name = "test_py_functions_failed" if self.is_test else "py_functions_failed"
    collection = mongo_driver.get_collection(self.dataset, collection_name)
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "name")
    collection.insert(function_json)

  def is_invalid_py_function(self, function_name):
    collection_name = "test_py_functions_failed" if self.is_test else "py_functions_failed"
    collection = mongo_driver.get_collection(self.dataset, collection_name)
    return collection.find_one({"name": function_name}) is not None

  def load_py_functions(self):
    collection_name = "test_py_functions_executed" if self.is_test else "py_functions_executed"
    collection = mongo_driver.get_collection(self.dataset, collection_name)
    return collection.find()

  def save_py_metadata(self, func_json):
    collection = mongo_driver.get_collection(self.dataset, "py_functions_metadata")
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "name")
    if mongo_driver.contains_document(collection, "name", func_json["name"]):
      mongo_driver.delete_document(collection, "name", func_json["name"])
    collection.insert(func_json)

  def load_py_metadata(self, function_name):
    try:
      collection = mongo_driver.get_collection(self.dataset, "py_functions_metadata")
      return collection.find_one({"name": function_name})
    except Exception:
      LOGGER.exception("Failed to metadata for function: '%s'. Returning None" % function_name)
      return None

  def get_executed_functions(self, language):
    collection = mongo_driver.get_collection(self.dataset, "language_executed_functions")
    document = collection.find_one({"language": language})
    if document is None:
      return None
    return document['names']



class PyFileMetaStore(base_store.PyFileMetaStore):
  def __init__(self, dataset, **kwargs):
    base_store.PyFileMetaStore.__init__(self, dataset,  **kwargs)

  def load_meta(self, file_name):
    sep_positions = [m.start() for m in re.finditer(os.sep, file_name)]
    if sep_positions and len(sep_positions) > 3:
      fp_regex = file_name[sep_positions[2]:]
    else:
      fp_regex = file_name
    collection = mongo_driver.get_collection(self.dataset, "py_file_meta")
    return collection.find_one({"file_path": {"$regex": fp_regex}})

  def save_meta(self, bson_dict):
    collection = mongo_driver.get_collection(self.dataset, "py_file_meta")
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "file_path")
    collection.insert(bson_dict)


class ArgumentStore(base_store.ArgumentStore):
  def __init__(self, dataset, **kwargs):
    self.is_test = None
    base_store.ArgumentStore.__init__(self, dataset, **kwargs)

  def load_args(self, args_key):
    collection_name = "test_fuzzed_args" if self.is_test else "fuzzed_args"
    collection = mongo_driver.get_collection(self.dataset, collection_name)
    try:
      return collection.find_one({"key": args_key})
    except Exception as e:
      LOGGER.exception("Failed to load args with key: '%s'. Returning None" % args_key)
      return None


class ExecutionStore(base_store.ExecutionStore):
  def __init__(self, dataset, **kwargs):
    base_store.ExecutionStore.__init__(self, dataset, **kwargs)

  def save_language_executed_function_names(self, language, names):
    collection = mongo_driver.get_collection(self.dataset, "language_executed_functions")
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "language")
    if mongo_driver.contains_document(collection, "language", language):
      mongo_driver.delete_document(collection, "language", language)
    collection.insert({
      "language": language,
      "names": names
    })

  def save_cloned_function_names(self, name, clones):
    collection = mongo_driver.get_collection(self.dataset, "cloned_functions")
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "_function_name_")
    if mongo_driver.contains_document(collection, "_function_name_", name):
      mongo_driver.delete_document(collection, "_function_name_", name)
    clones["_function_name_"] = name
    collection.insert(clones)

  def load_cloned_function_names(self, name):
    collection = mongo_driver.get_collection(self.dataset, "cloned_functions")
    return mongo_driver.get_document(collection, "_function_name_", name)


class ClusterStore(base_store.ClusterStore):
  def __init__(self, dataset, **kwargs):
    base_store.ClusterStore.__init__(self, dataset,  **kwargs)

  def save_clusters(self, clusters, suffix):
    collection_name = "clusters_%s" % suffix
    collection = mongo_driver.get_collection(self.dataset, collection_name)
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "cluster_id")
    for cluster_id, functions in clusters.items():
      LOGGER.info("Saving cluster: '%d', with %d functions"  % (cluster_id, len(functions)))
      cluster = {
        "cluster_id": cluster_id,
        "functions": [lib.to_json(f) for f in functions]
      }
      collection.insert(cluster)


