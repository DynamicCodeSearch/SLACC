from __future__ import print_function, division
import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from collections import defaultdict

class UnionFind:
  def __init__(self, points):
    self._id = {}
    self._sz = {}
    self.ref = {}
    self.rev_ref = {}
    for i, point in enumerate(points):
      self._id[i] = i
      self._sz[i] = 1
      self.ref[i] = point
      self.rev_ref[id(point)] = i

  def _root(self, point):
    j = self.rev_ref[id(point)]
    while j != self._id[j]:
      self._id[j] = self._id[self._id[j]]
      j = self._id[j]
    return j

  def find(self, p, q):
    return self._root(p) == self._root(q)

  def union(self, p, q):
    i = self._root(p)
    j = self._root(q)
    if i == j: return
    if self._sz[i] < self._sz[j]:
      self._id[i] = j
      self._sz[j] += self._sz[i]
    else:
      self._id[j] = i
      self._sz[i] += self._sz[j]


  def get_clusters(self):
    clusters = defaultdict(list)
    for p_id, c_id in self._id.items():
      clusters[c_id].append(self.ref[p_id])
    return clusters.values()