import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from collections import defaultdict
import re

from sos import similarity
from store import mongo_store
from sos.function import Function, Outputs
from utils import lib, cache, logger
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


def get_cross_val(dataset, n_folds):
  functions = similarity.load_functions(dataset, is_test=True) + similarity.load_py_functions(dataset, is_test=True)
  all_outputs = [func.outputs for func in functions]
  folds = []
  fold_size = len(all_outputs[0].returns) // n_folds
  for i in range(n_folds):
    fold = []
    start, end = i * fold_size, (i + 1) * fold_size
    for func in functions:
      clone = func.deep_clone()
      clone.outputs = all_outputs[i].subset(start, end)
      fold.append(clone)
    folds.append(fold)
  return folds


def random_testing(dataset, n_folds=10):
  LOGGER.info("Random testing with '%d' number of folds" % n_folds)
  folds = get_cross_val(dataset, n_folds)
  base_folder = lib.get_clusters_folder(dataset)
  file_name = "java_python"
  for index, fold in enumerate(folds):
    result_folder = os.path.join(base_folder, "random_testing", "fold_%d" % index)
    LOGGER.info("Random testing for for fold '%d' out of '%d'" % (index + 1, n_folds))
    similarity.compute_similarity(dataset, functions=fold, base_folder=result_folder, file_name=file_name, skip_singles=True)

  # print(len(functions))


def _help():
  return """
  Format:
    python sos/similarity <utility> <dataset> <?additional_args>
    utility: save_function_names/random_testing
    dataset: codejam/introclass
    additional_args
      language: java(default)/python/java_python
      n_folds: default(10)
    """


def _main():
  args = sys.argv
  if len(args) < 3:
    print(_help())
    exit(0)
  utility, dataset = args[1], args[2]
  if utility == "save_function_names":
    language = args[3] if len(args) >= 4 else "java"
    save_clustered_function_names(dataset, language)
  elif utility == "random_testing":
    n_folds = int(args[3]) if len(args) >= 4 else 10
    random_testing(dataset, n_folds)
  else:
    print("Invalid utility: %s" % utility)
    print(_help())


if __name__ == "__main__":
  _main()
  # validate("codejam")