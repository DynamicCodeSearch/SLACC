from __future__ import print_function, division
import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from collections import defaultdict
from sklearn.cluster import DBSCAN
import numpy as np
import re

from function import Function, Outputs
from utils import cache, logger, lib
from utils.lib import O
from utils.stat import Stat

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def load_functions_for_class(class_json_file, dataset):

  def get_package(json_file):
    return json_file.split("%sfunctions%s" %
                           (os.path.sep, os.path.sep))[-1].rsplit(os.path.sep, 1)[0].replace(os.path.sep, ".")

  class_json = cache.load_json(class_json_file)
  class_name = cache.get_file_name(class_json_file)
  package = get_package(class_json_file)
  functions = []
  function_pattern = re.compile(r'^func_')
  class_metadata = load_class_metadata(dataset, package, class_name)
  for function_name, details in class_json.items():
    if not function_pattern.match(function_name):
      continue
    function_metadata = class_metadata[function_name]
    return_meta_data = function_metadata["return"]
    outputs = Outputs(details["outputs"])
    funct = Function(name=function_name, dataset=dataset,
                     class_name=class_name, package=package,
                     input_key=details["inputKey"], outputs=outputs,
                     lines_touched=function_metadata.get("linesTouched", None),
                     span=function_metadata.get("span", None), body=function_metadata["body"])
    if is_object_return(return_meta_data):
      for attribute, returns in get_return_vals(outputs.returns).items():
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


def is_object_return(metadata):
  """
  Is the return type of object
  :param metadata:
  :return:
  """
  return not metadata["isArray"] and not metadata["isPrimitive"]


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


def load_class_metadata(dataset, package, class_name):
  metadata_file = os.path.join(lib.get_dataset_meta_results_folder(dataset), package.replace(".", os.path.sep),
                               "%s.json" % class_name)
  return cache.load_json(metadata_file)


def load_functions(dataset):
  functions = []
  results_folder = lib.get_dataset_functions_results_folder(dataset)
  for json_file in lib.list_files(results_folder, check_nest=True, is_absolute=True):
    if not json_file.endswith(".json"):
      continue
    functions += load_functions_for_class(json_file, dataset)
  valid_functions = [func for func in functions if func.is_useful()]
  LOGGER.info("Valid Functions : %d / %d" % (len(valid_functions), len(functions)))
  return valid_functions


def execution_similarity(func1, func2):
  if func1.input_key != func2.input_key:
    return 0.0
  sames = 0.0
  alls = 0.0
  assert len(func1.outputs.returns) == len(func2.outputs.returns)
  for i in xrange(len(func1.outputs.returns)):
    alls += 1
    o1 = func1.outputs.returns[i]
    o2 = func2.outputs.returns[i]
    e1 = func1.outputs.errors[i]
    e2 = func2.outputs.errors[i]
    if o1 == o2 and e1 == e2:
      sames += 1
  return sames / alls


def execution_distance(func1, func2):
  return 1.0 - execution_similarity(func1, func2)


class Clusterer(O):
  def __init__(self, functions, **kwargs):
    self.functions = functions
    self.X = np.arange(len(self.functions)).reshape(-1, 1)
    O.__init__(self, **kwargs)

  def distance(self, x, y):
    return execution_distance(self.functions[int(x)], self.functions[int(y)])

  def cluster(self, file_name=None):
    dbs = DBSCAN(eps=0.01, min_samples=2, metric=self.distance)
    labels = dbs.fit_predict(self.X)
    clusters = defaultdict(list)
    for label, func in zip(labels, self.functions):
      clusters[label].append(func)
    file_contents = []
    for label, func_cluster in clusters.items():
      if label == -1: continue
      cluster_str = "\n\n****** Cluster %d ******" % label
      if file_name is not None: file_contents.append(cluster_str)
      for func in func_cluster:
        if file_name is not None: file_contents.append(func.body)
      # print(file_contents)
      cache.write_file(file_name, "\n".join(file_contents))
    return clusters


def similarity_for_dataset(dataset):
  functions = load_functions(dataset)
  clusters_txt_file = os.path.join(lib.get_clusters_folder(dataset), "codejam.txt")
  clusters_pkl_file = os.path.join(lib.get_clusters_folder(dataset), "codejam.pkl")
  clusters = Clusterer(functions).cluster(clusters_txt_file)
  cache.save_pickle(clusters_pkl_file, clusters)
  n_clusters = len(clusters)
  sizes = [len(cluster_funcs) for label, cluster_funcs in clusters.items() if label != -1]
  LOGGER.info("## Cluster sizes")
  LOGGER.info("### Number of clusters: %d" % n_clusters)
  LOGGER.info("### Number of functions clustered: %d" % sum(sizes))
  LOGGER.info("### Number of functions not clustered: %d" % (len(functions) - sum(sizes)))
  Stat(sizes).report()


def similarity_for_introclass():
  similarity_for_dataset("introclass")


def similarity_for_codejam():
  similarity_for_dataset("codejam")


def _test():
  functions = load_functions("/Users/panzer/Raise/ProgramRepair/CodeSeer/code/meta_results/CodeJam/Y11R5P1/Egor/generated_class_40017a204724451689624d13b72a23fe.json", "Y11R5P1", "Egor")
  count = 0
  for funct in functions:
    if funct.name == "func_a91e1656934842209b5dc8b5fddbe8af":
      count += 1
  print(count)


if __name__ == "__main__":
  args = sys.argv
  if len(args) < 2:
    print("Provide a dataset")
    exit(0)
  if args[1] == "codejam":
    similarity_for_codejam()
  elif args[1] == "introclass":
    similarity_for_introclass()
  else:
    print("Invalid dataset : %s" % args[1])
