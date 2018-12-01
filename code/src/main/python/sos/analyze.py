import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from collections import defaultdict

from utils import lib, cache, logger
from store import mongo_store
import properties


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def get_cluster_path(dataset, language):
  return os.path.join(lib.get_clusters_folder(dataset), "%s.pkl" % language)


def get_execution_store(dataset):
  if properties.STORE == "mongo":
    return mongo_store.ExecutionStore(dataset)
  raise RuntimeError("Invalid configuration: %s" % properties.STORE)


def save_clustered_function_names(dataset, language):
  LOGGER.info("Saving clustered function names for dataset '%s' and language '%s'" % (dataset, language))
  cluster_path = get_cluster_path(dataset, language)
  clusters = cache.load_pickle(cluster_path)
  function_names = defaultdict(set)
  cloned_functions = defaultdict(dict)
  for label, functions in clusters.items():
    if label == -1: continue
    for funct in functions:
      name, clone_name, clone_attribute = None, None, None
      lang = funct.source
      if hasattr(funct, "base_name") and funct.base_name is not None:
        name = funct.base_name
        clone_name = funct.name
        clone_attribute = funct.return_attribute
      else:
        name = funct.name
      function_names[lang].add(name)
      if clone_name:
        cloned_functions[name][clone_attribute] = clone_name
  execution_store = get_execution_store(dataset)
  for lang, names in function_names.items():
    execution_store.save_language_executed_function_names(lang, list(names))
  for name, clones in cloned_functions.items():
    execution_store.save_cloned_function_names(name, clones)


def _help():
  return """
  Format:
    python sos/similarity <utility> <dataset> <language>
    utility: save_function_names
    dataset: codejam/introclass
    language: java(default)/python/java_python
    """


def _main():
  args = sys.argv
  if len(args) < 4:
    print(_help())
    exit(0)
  utility, dataset, language = args[1], args[2], args[3]
  if utility == "save_function_names":
    save_clustered_function_names(dataset, language)
  else:
    print("Invalid utility: %s" % utility)
    print(_help())


if __name__ == "__main__":
  _main()
