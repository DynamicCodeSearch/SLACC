import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from collections import defaultdict
import csv
import networkx

from sos import similarity, clusterer
from store import mongo_store
from utils import lib, cache, logger
from utils.stat import Stat
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


def get_cross_val(dataset, n_folds, as_dict=False):
  functions = similarity.load_functions(dataset, is_test=True) + similarity.load_py_functions(dataset, is_test=True)
  all_outputs = [func.outputs for func in functions]
  folds = []
  fold_size = len(all_outputs[0].returns) // n_folds
  for i in range(n_folds):
    fold = {} if as_dict else []
    start, end = i * fold_size, (i + 1) * fold_size
    for func in functions:
      clone = func.deep_clone()
      clone.outputs = all_outputs[i].subset(start, end)
      if as_dict:
        fold[clone.name] = clone
      else:
        fold.append(clone)
    folds.append(fold)
  return folds


# def random_testing(dataset, n_folds=10):
#   LOGGER.info("Random testing with '%d' number of folds" % n_folds)
#   folds = get_cross_val(dataset, n_folds)
#   base_folder = lib.get_clusters_folder(dataset)
#   file_name = "java_python"
#   for index, fold in enumerate(folds):
#     result_folder = os.path.join(base_folder, "random_testing", "fold_%d" % index)
#     LOGGER.info("Random testing for for fold '%d' out of '%d'" % (index + 1, n_folds))
#     clusterer = similarity.Clusterer(fold)
#     print(clusterer.distance(0, 1))
#     # print(fold[0].outputs.returns[:10])
#     # similarity.compute_similarity(dataset, functions=fold, base_folder=result_folder, file_name=file_name, skip_singles=True)
#   exit(0)


def random_testing(dataset, language="java_python", n_folds=10):
  LOGGER.info("Random testing with '%d' number of folds" % n_folds)
  folds = get_cross_val(dataset, n_folds, as_dict=True)
  base_folder = lib.get_clusters_folder(dataset)
  LOGGER.info("Loading pickle ...")
  cluster_path = get_cluster_path(dataset, language)
  clusters = cache.load_pickle(cluster_path)
  for index, fold in enumerate(folds):
    file_name = os.path.join(base_folder, "random_testing", "fold_%d" % index, "distances.pkl")
    cluster_distances = {}
    for label, functions in clusters.items():
      if label == -1:
        continue
      similarity_map = defaultdict(dict)
      for i in range(len(functions) - 1):
        for j in range(i + 1, len(functions)):
          assert i != j
          f_i, f_j = functions[i], functions[j]
          distance = clusterer.execution_distance(fold[f_i.name], fold[f_j.name])
          similarity_map[f_i.name][f_j.name] = distance
          similarity_map[f_j.name][f_i.name] = distance
      cluster_distances[label] = similarity_map
    cache.save_pickle(file_name, cluster_distances)


def cluster_testing(dataset, language="java_python"):
  LOGGER.info("Testing different cluster sizes for dataset '%s' and language '%s'" % (dataset, language))
  functions = similarity.load_functions(dataset) + similarity.load_py_functions(dataset)
  errors = [0.01, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30]
  base_folder = os.path.join(lib.get_clusters_folder(dataset), "cluster_testing")
  for clustering_error in errors:
    result_folder = os.path.join(base_folder, "eps_%0.2f" % clustering_error)
    similarity.compute_similarity(dataset, language, functions=functions, base_folder=result_folder,
                                  clustering_error=clustering_error, cluster_suffix="%0.2f" % clustering_error)


def cluster_source(dataset, language="java_python"):
  LOGGER.info("Loading pickle ...")
  cluster_path = get_cluster_path(dataset, language)
  clusters = cache.load_pickle(cluster_path)
  cluster_type_counts = defaultdict(int)
  for label, functions in clusters.items():
    if label == -1:
      continue
    contains_java = False
    contains_python = False
    for func in functions:
      if func.source == "java":
        contains_java = True
      elif func.source == "python":
        contains_python = True
    if contains_python and contains_java:
      cluster_type_counts["mixed"] += 1
    elif contains_java:
      cluster_type_counts["java"] += 1
    elif contains_python:
      cluster_type_counts["python"] += 1
  print(cluster_type_counts)


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


def save_only_target_functions(dataset, mixed_file_base_name, target_language):
  """
  Save only java functions from a mixture of java and python clusters
  :param dataset: Name of dataset
  :param mixed_file_base_name: Type of language eg. java_python
  :param target_language: Target Language
  :return:
  """
  clusters_base_folder = os.path.join(lib.get_clusters_folder(dataset), "cluster_testing")
  for folder in sorted(cache.list_dir(clusters_base_folder, is_absolute=False)):
    LOGGER.info("Processing '%s' ..." % folder)
    folder_path = os.path.join(clusters_base_folder, folder)
    cache.mkdir(folder_path)
    base_clusters_file = os.path.join(folder_path, "%s.pkl" % mixed_file_base_name)
    base_clusters = cache.load_pickle(base_clusters_file)
    target_clusters = {}
    for label, functions in base_clusters.items():
      if label == -1 or len(functions) == 1: continue
      contains_target = False
      contains_other = False
      for func in functions:
        if func.source == target_language:
          contains_target = True
        else:
          contains_other = True
      if contains_target and not contains_other:
        target_clusters[label] = functions
    LOGGER.info("For folder = %s, # of '%s' clusters = %d" % (folder, target_language, len(target_clusters)))
    file_path = os.path.join(folder_path, "only_%s.txt" % target_language)
    pkl_path = os.path.join(folder_path, "only_%s.pkl" % target_language)
    file_contents = []
    for label, functions in target_clusters.items():
      file_contents.append("\n\n****** Cluster %d ******" % label)
      for func in functions:
        file_contents.append(func.body)
    cache.write_file(file_path, "\n".join(file_contents))
    cache.save_pickle(pkl_path, target_clusters)


def save_only_mixed_clusters(dataset, mixed_file_base_name):
  """
  Save only mixed functions
  :param dataset: Name of dataset
  :param mixed_file_base_name: Type of language eg. java_python
  :return:
  """
  clusters_base_folder = os.path.join(lib.get_clusters_folder(dataset), "cluster_testing")
  for folder in sorted(cache.list_dir(clusters_base_folder, is_absolute=False)):
    LOGGER.info("Processing '%s' ..." % folder)
    folder_path = os.path.join(clusters_base_folder, folder)
    cache.mkdir(folder_path)
    base_clusters_file = os.path.join(folder_path, "%s.pkl" % mixed_file_base_name)
    base_clusters = cache.load_pickle(base_clusters_file)
    mixed_clusters = {}
    for label, functions in base_clusters.items():
      if label == -1 or len(functions) == 1: continue
      sources = set()
      for func in functions:
        sources.add(func.source)
      if len(sources) > 1:
        mixed_clusters[label] = functions
    LOGGER.info("For folder = %s, # of mixed clusters = %d" % (folder, len(mixed_clusters)))
    file_path = os.path.join(folder_path, "only_mixed.txt")
    pkl_path = os.path.join(folder_path, "only_mixed.pkl")
    file_contents = []
    for label, functions in mixed_clusters.items():
      file_contents.append("\n\n****** Cluster %d ******" % label)
      for func in functions:
        file_contents.append(func.body)
    cache.write_file(file_path, "\n".join(file_contents))
    cache.save_pickle(pkl_path, mixed_clusters)


def connected_components(dataset, base_folder):
  base_folder_path = os.path.join(properties.META_RESULTS_FOLDER, dataset, base_folder)
  contents = ["# Epsilons and methods"]
  for file_path in sorted(cache.list_files(base_folder_path, is_absolute=True)):
    if not file_path.endswith(".csv"):
      continue
    epsilon = cache.get_file_name(file_path).split(".")[0].split("_", 1)[1].replace("_", ".")
    print(file_path)
    graph = networkx.Graph()
    contents.append("## eps = %s" % epsilon)
    with open(file_path) as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=",")
      next(csv_reader, None)
      for row in csv_reader:
        graph.add_edge(row[0], row[1])
      n_clusters = networkx.number_connected_components(graph)
      contents.append("#### \# Functionalities = %d" % n_clusters)
      contents.append("```")
      [contents.append("%d: %s" % (i, ",\n\t".join(component)))
       for i, component in enumerate(networkx.connected_components(graph))]
      # [contents.append("%d: %s" % (i, ",".join(map(str, sorted(map(int, component))))))
      #  for i, component in enumerate(networkx.connected_components(graph))]
      contents.append("```")
    LOGGER.info("For epsilon = %s, # clusters = %d" % (epsilon, n_clusters))
  write_file = os.path.join(base_folder_path, "components.md")
  cache.write_file(write_file, "\n".join(contents))


def get_class_and_generate_functions(dataset, language="java_python", eps=0.01):
  base_file = os.path.join(properties.META_RESULTS_FOLDER, dataset, "clusters", "cluster_testing",
                           "eps_%0.2f" % eps, "%s.pkl" % language)
  clusters = cache.load_pickle(base_file)
  packages = set()
  for label, functions in clusters.items():
    if label == -1 or len(functions) == 1: continue
    for func in functions:
      if func.source == "java":
        packages.add(func.package)
  for package in sorted(list(packages)):
    print(package)


def overlaps(func_a_meta, func_b_meta):
  if func_a_meta['baseFilePath'] != func_b_meta['baseFilePath']:
    return False
  a_span = set(func_a_meta['span'])
  b_span = set(func_b_meta['span'])
  return len(a_span.intersection(b_span)) > 0


def is_more_succinct(func_a_meta, func_b_meta):
  a_span = set(func_a_meta['span'])
  b_span = set(func_b_meta['span'])
  return a_span < b_span


def remove_overlapping_clusters(dataset, language="java_python"):
  # TODO: Think about how to remove syntactic equivalence
  store = mongo_store.FunctionStore(dataset)
  base_file = os.path.join(properties.META_RESULTS_FOLDER, dataset, "clusters", "%s.pkl" % language)
  clusters = cache.load_pickle(base_file)
  non_overlapping_clusters = {}
  for label, functions in clusters.items():
    if label == -1 or len(functions) == 1: continue
    non_overlapping_funcs = []
    metas = {}
    for func in functions:
      meta = store.load_metadata({"name": func.base_name})
      metas[func.base_name] = meta
      if len(non_overlapping_funcs) == 0:
        non_overlapping_funcs.append(func)
        continue
      is_non_overlapping_funcs_updated = False
      for i, existing_func in enumerate(non_overlapping_funcs):
        existing_meta = metas[existing_func.base_name]
        if overlaps(meta, existing_meta):
          is_non_overlapping_funcs_updated = True
          if is_more_succinct(meta, existing_meta):
            non_overlapping_funcs[i] = func
          break
      if not is_non_overlapping_funcs_updated:
        non_overlapping_funcs.append(func)
    if len(non_overlapping_funcs) > 1:
      non_overlapping_clusters[label] = non_overlapping_funcs
  write_folder = os.path.join(properties.META_RESULTS_FOLDER, dataset, "clusters", "non_overlapping")
  cache.mkdir(write_folder)
  clusters_txt_file = os.path.join(write_folder, "%s.txt" % language)
  clusters_pkl_file = os.path.join(write_folder, "%s.pkl" % language)
  clusters_report_file = os.path.join(write_folder, "%s.md" % language)
  cache.save_pickle(clusters_pkl_file, non_overlapping_clusters)
  clusterer.save_clusters_to_db(dataset, non_overlapping_clusters, "non_overlapping")
  clusterer.save_clusters_to_txt(non_overlapping_clusters, clusters_txt_file)
  sizes = [len(cluster_funcs) for label, cluster_funcs in non_overlapping_clusters.items() if label != -1]
  meta_data = "## Cluster sizes\n"
  meta_data += "* Number of clusters: %d\n" % len(non_overlapping_clusters)
  meta_data += "* Number of functions clustered: %d\n" % sum(sizes)
  meta_data += "## REPORT\n"
  meta_data += Stat(sizes).report()
  cache.write_file(clusters_report_file, meta_data)


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
    random_testing(dataset, n_folds=n_folds)
  elif utility == "cluster_testing":
    language = args[3] if len(args) >= 4 else "java"
    cluster_testing(dataset, language)
  elif utility == "save_target":
    if len(args) < 5:
      print("""
      Format: python sos/similarity <utility> <dataset> <mixed_file_base_name> <target_language>
        eg. python sos/similarity <utility> <dataset> java_python java""")
      exit()
    save_only_target_functions(dataset, args[3], args[4])
  elif utility == "save_mixed":
    if len(args) < 4:
      print("""
      Format: python sos/similarity <utility> <dataset> <mixed_file_base_name>
        eg. python sos/similarity <utility> <dataset> java_python""")
      exit()
    save_only_mixed_clusters(dataset, args[3])
  else:
    print("Invalid utility: %s" % utility)
    print(_help())


def _test():
  # save_only_java_functions("codejam")
  # connected_components("codejam", "HitoshiIO")
  # cluster_source("codejam")
  # random_testing2("codejam")
  # validate("codejam")
  # get_class_and_generate_functions("codejam")
  remove_overlapping_clusters("IntroClassJava", "java")
  pass


if __name__ == "__main__":
  _main()
