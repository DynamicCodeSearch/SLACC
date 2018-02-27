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

FUNCTION_FILE = "data/cfiles_dump/fuzzed/uniform.pkl"


class Point(O):
  def __init__(self):
    O.__init__(self)
    self.outputs = []
    self.errors = []

  @staticmethod
  def from_function(function):
    if function['results'] is None: return None
    point = Point()
    for result in function['results']:
      if result[1] is not None:
        point.outputs.append(result[1])
      else:
        point.errors.append(result[2])
    point.function_body = function['function'].body
    return point


def pre_process(functions):
  points = []
  for function in functions.values():
    point = Point.from_function(function)
    if point is not None:
      points.append(point)
  return points


def distribution_dist(a, b):
  # TODO: Create a custom distribution and add it to cluster class.
  return 1


def _main():
  functions = cache.load(FUNCTION_FILE)
  points = pre_process(functions)
  dbscan(np.arange(len(points)).reshape(-1, 1), metric=distribution_dist, eps=5, min_samples=2)
  # TODO: Create a class for dbscan and use that to cluser with a custom metric



if __name__ == "__main__":
  _main()