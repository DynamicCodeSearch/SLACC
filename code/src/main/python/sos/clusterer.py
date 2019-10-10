import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from collections import defaultdict
from sklearn.cluster import DBSCAN
import numpy as np

from utils import cache, logger, uf, lib
from utils.lib import O
from store import mongo_store


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def execution_similarity(func1, func2):
  if func1.input_key != func2.input_key:
    return 0.0
  sames = 0.0
  alls = 0.0
  assert len(func1.outputs.returns) == len(func2.outputs.returns)
  for i in range(len(func1.outputs.returns)):
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


def save_clusters_to_txt(clusters, file_name):
  file_contents = []
  for label, func_cluster in clusters.items():
    if label == -1: continue
    cluster_str = "\n\n****** Cluster %d ******" % label
    file_contents.append(cluster_str)
    for func in func_cluster:
      file_contents.append(func.body)
  cache.write_file(file_name, "\n".join(file_contents))


def save_clusters_to_db(dataset, clusters, suffix):
  store = mongo_store.ClusterStore(dataset)
  store.save_clusters(clusters, suffix)


def load_clusters_from_pkl(file_name):
  return cache.load_pickle(file_name)


def _transfer_clusters(dataset):
  file_name = os.path.join(lib.get_clusters_folder(dataset), "java.pkl")
  clusters = load_clusters_from_pkl(file_name)
  save_clusters_to_db(dataset, clusters, "base")


class DBScanClusterer(O):
  def __init__(self, functions, **kwargs):
    self.functions = functions
    # noinspection PyUnresolvedReferences
    self.X = np.arange(len(self.functions)).reshape(-1, 1)
    O.__init__(self, **kwargs)

  def distance(self, x, y):
    return execution_distance(self.functions[int(x)], self.functions[int(y)])

  def cluster(self, file_name=None, skip_singles=False, clustering_error=0.01):
    LOGGER.info("Clustering using DBScan with tolerance '%0.2f'" % clustering_error)
    dbs = DBSCAN(eps=clustering_error, min_samples=2, metric=self.distance)
    labels = dbs.fit_predict(self.X)
    clusters = defaultdict(list)
    for label, func in zip(labels, self.functions):
      if skip_singles and label == -1:
        continue
      clusters[label].append(func)
    save_clusters_to_txt(clusters, file_name)
    return clusters


class RepresentativeClusterer(O):
  def __init__(self, functions, distance_function=execution_distance, **kwargs):
    self.functions = functions
    self.distance_function = distance_function
    self.union_find = uf.UnionFind(functions)
    O.__init__(self, **kwargs)

  def cluster(self, file_name=None, skip_singles=False, clustering_error=0.01):
    LOGGER.info("Clustering using Representative Sampling with tolerance '%0.2f'" % clustering_error)
    n = len(self.functions)
    for i in xrange(n - 1):
      LOGGER.info("Processing function %d / %d " % (i + 1, n - 1))
      for j in xrange(i+1, n):
        f_i = self.functions[i]
        f_j = self.functions[j]
        if self.union_find.find(f_i) == self.union_find.find(f_j):
          continue
        dist = self.distance_function(f_i, f_j)
        if dist <= clustering_error:
          self.union_find.union(f_i, f_j)
    clusters = {}
    for cluster_id, functions in self.union_find.get_disjoint_sets().items():
      if skip_singles and len(functions) == 1:
        continue
      clusters[cluster_id] = functions
    save_clusters_to_txt(clusters, file_name)
    return clusters


if __name__ == "__main__":
  _transfer_clusters("IntroClassJava")
