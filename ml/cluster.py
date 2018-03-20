from __future__ import print_function, division
import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from utils import cache
from utils.lib import O
from sklearn.cluster import dbscan
import numpy as np
import scipy as sp
from scipy import stats
from collections import defaultdict
from utils.uf import UnionFind
import argparse
from joblib import Parallel, delayed
from utils.logger import get_logger
import matplotlib.pyplot as plt
import logging

FUNCTION_FILE = "data/cfiles_dump/fuzzed/uniform.pkl"
LOG_LEVEL = logging.INFO
logger = get_logger(__name__, LOG_LEVEL)


def get_file_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("-n", "--n_jobs", type=int, default=2, help="Number of jobs")
  parser.add_argument("-f", "--function", type=str, default="oops", help="Fuzz functions")
  return parser.parse_args()


class Point(O):
  def __init__(self):
    O.__init__(self)
    self.outputs = []
    self.errors = []
    self.arguments = []
    self.function_body = None
    self.function_name = None
    self.arg_types = []
    self.return_type = None
    self.cluster_id = None


  @staticmethod
  def from_function(function):
    if function['results'] is None: return None
    point = Point()
    for result in function['results']:
      point.arguments.append(result[0])
      point.outputs.append(result[1])
      point.errors.append(result[2])
      # if result[1] is not None:
      #   point.outputs.append(result[1])
      # else:
      #   point.errors.append(result[2])
    # point.outputs = function['results']
    # point.errors = function['errors']
    point.arg_types = [arg.type for arg in function['function'].args]
    point.function_name = function['function'].name
    point.function_body = function['function'].body
    point.return_type = function['function'].ret.type
    return point

  @staticmethod
  def equal(a, b):
    if a.return_type != b.return_type: return False
    if a.arg_types != b.arg_types: return False
    if a.arguments != b.arguments: return False
    return a.outputs == b.outputs


class Clusterer(O):
  def __init__(self, functions):
    O.__init__(self)
    self.points = pre_process(functions)
    self.X = np.arange(len(self.points)).reshape(-1, 1)

  def distance(self, x, y):
    point_a = self.points[int(x)]
    point_b = self.points[int(y)]
    if point_a.return_type != point_b.return_type:
      return 1
    return 1

  def cosine_distance(self, x, y):
    point_a = self.points[int(x)]
    point_b = self.points[int(y)]
    a_outputs = set(point_a.outputs)
    b_outputs = set(point_b.outputs)
    all_words = set().union(a_outputs).union(b_outputs)
    a_vector, b_vector = [], []
    for word in all_words:
      a_vector.append(1 if word in a_outputs else 0)
      b_vector.append(1 if word in b_outputs else 0)
    return np.dot(a_vector, b_vector) / (np.linalg.norm(a_vector) * np.linalg.norm(b_vector))

  def ks_distance(self, x, y):
    point_a = self.points[int(x)]
    point_b = self.points[int(y)]
    a_outputs = point_a.outputs
    b_outputs = point_b.outputs
    if len(a_outputs) == 0 or len(b_outputs) == 0:
      return 1.0
    similarity, significance = stats.ks_2samp(a_outputs, b_outputs)
    if significance > 0.1:
      return 1.0 - similarity
    return 1.0

  def cluster(self):
    ret_groups = defaultdict(list)
    rets = set()
    arguments = {
        "float": (self.ks_distance, 0.25, 2),
        "int": (self.ks_distance, 0.025, 5),
        "char": (self.ks_distance, 0.5, 2)
    }
    ret_points = defaultdict(list)
    for point, x in zip(self.points, self.X):
      rets.add(point.return_type)
      ret_groups[point.return_type].append(x)
      ret_points[point.return_type].append(point)
    for ret_type, group in ret_groups.items():
      argument = arguments[ret_type]
      _, cluster_labels = dbscan(group, metric=argument[0], eps=argument[1], min_samples=argument[2])
      noise = sum([1 if label == -1 else 0 for label in cluster_labels])
      for point, cluster_label in zip(ret_points[ret_type], cluster_labels):
        if cluster_label == -1:
          point.cluster_id = "OUTLIER"
        else:
          point.cluster_id = "%s-%d" % (ret_type, cluster_label)
      print(ret_type, len(group), noise, set(cluster_labels))
    point_clusters = []
    for points in ret_points.items():
      point_clusters.append(points)
    cache.save("data/cfiles_dump/clusters/dbscan.pkl", point_clusters)

  def clones(self, destination_folder, n_jobs):
    ret_groups = defaultdict(list)
    ret_points = defaultdict(list)
    rets = set()
    logger.info("Sorting by return types")
    for point, x in zip(self.points, self.X):
      rets.add(point.return_type)
      ret_groups[point.return_type].append(x)
      ret_points[point.return_type].append(point)
    logger.info("Return Types: %s" % rets)
    Parallel(n_jobs=n_jobs)(delayed(union_find)(ret_type, points, destination_folder) for ret_type, points in ret_points.items())


def union_find(ret_type, points, destination_folder):
  logger.info("Identifying clones for %s" % ret_type)
  uf = UnionFind(points)
  for i, p in enumerate(points):
    if len(p.outputs) == 0: continue
    if i % 100 == 0:
      logger.info("In %s; Processed %d/%d functions" % (ret_type, i, len(points)))
    for q in uf.get_representatives():
    # for q in points:
      if uf.find(p, q): continue
      # if set(p.outputs) == set(q.outputs):
      if Point.equal(p, q):
        uf.union(p, q)
  # Bookmarks for stats
  direct_clones = []
  grouped = 0
  outputs_in_clusters = defaultdict(int)
  methods_in_clusters = defaultdict(int)
  for cluster in uf.get_clusters():
    if len(cluster) > 1:
      ## Test
      # for i in range(min(3, len(cluster))):
      #   print(cluster[i].function_body)
      #   print(cluster[i].outputs)
      # exit()
      output_size = len(set(cluster[0].outputs))
      if output_size >= 7:
        output_size = "7+"
      outputs_in_clusters[output_size] += 1
      methods_in_clusters[output_size] += len(cluster)
      grouped += len(cluster)
      direct_clones.append(cluster)
  result = O(
    ret_type=ret_type,
    n_methods=len(points),
    n_direct_clones_cluster=len(direct_clones),
    n_no_clones=len(points) - grouped,
    num_clusters_wrt_size=outputs_in_clusters,
    num_methods_in_clusters_wrt_size=methods_in_clusters
  )
  print(result)
  destination_file = cache.create_file_path(destination_folder, ret_type, ext=".pkl")
  cache.save(destination_file, O(stats=result, clusters=direct_clones, uf=uf))


def plot_clone_cluster_sizes(root_folder):
  def bar_plot(x, y, save_file, title):
    x_i = np.arange(len(x))
    plt.bar(x_i, y)
    plt.xticks(x, x_i)
    plt.xlabel("# Clones in cluster")
    plt.ylabel("# Clusters")
    plt.ylim(0, max(y) + 1)
    plt.title(title)
    plt.savefig(save_file)
    plt.clf()

  sizes = defaultdict(int)
  for clone_file in cache.list_files(root_folder, is_relative=False):
    extension = clone_file.rsplit(".", 1)[-1]
    if extension != "pkl": continue
    data = cache.load(clone_file)
    for cluster in data.clusters:
      if len(set(cluster[0].outputs)) == 1: continue
      sizes[len(cluster)] += 1
  max_val = max(sizes.keys())
  x_axis = range(2, max_val + 1)
  y_axis = [sizes.get(x_val, 0) for x_val in x_axis]
  bar_plot(x_axis, y_axis, cache.create_file_path(root_folder, "cluster_sizes", ".png"),
           "Num of clusters vs Size of clusters")



def save_clone_clusters(root_folder, write_folder):
  cache.delete(write_folder)
  for clone_file in cache.list_files(root_folder, is_relative=False):
    data = cache.load(clone_file)
    ret_type = data.stats.ret_type
    counter = 0
    for cluster in data.clusters:
      cache.mkdir(write_folder)
      write_file_name = cache.create_file_path(write_folder, "clone_%s_%03d" % (ret_type, counter), ".txt")
      counter += 1
      with open(write_file_name, "wb") as f:
        for i, point in enumerate(cluster):
          f.write("\n\n/************ %03d : %s *************/\n\n" % (i, point.function_name))
          f.write(point.function_body)


def pre_process(functions):
  points = []
  for function in functions.values():
    point = Point.from_function(function)
    if point is not None:
      points.append(point)
  return points


def _create_clone(args):
  function_file = "data/cfiles_dump/valids_all/uniform_aggregate.pkl"
  destination_folder = "data/cfiles_dump/valids_all/clones"
  functions = cache.load(function_file)
  clusterer = Clusterer(functions)
  clusterer.clones(destination_folder, args.n_jobs)


def _save_clone_clusters():
  save_clone_clusters("data/cfiles_dump/valids_all/clones", "results/valids_all/clones")


def _main():
  args = get_file_args()
  f_name = args.function
  if f_name == "create_clone":
    _create_clone(args)
  elif f_name == "save_clone":
    _save_clone_clusters()
  else:
    print("WTF is %s!!!" % f_name)


if __name__ == "__main__":
  # _main()
  plot_clone_cluster_sizes("data/cfiles_dump/valids_all/clones")
