import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

'''
unionfind.py

A class that implements the Union Find data structure and algorithm.  This
data structure allows one to find out which set an object belongs to, as well
as join two sets.

The algorithm's performance, given m union/find operations of any ordering, on
n elements has been shown to take log* time per operation, where log* is
pronounced log-star, and is the INVERSE of what is known as the Ackerman
function, which is given below:
A(0) = 1
A(n) = 2**A(n-1)

I include the functions to be complete.  Note that we can be 'inefficient'
when performing the inverse ackerman function, as it will only take a maximum
of 6 iterations to perform; A(5) is 65536 binary digits long (a 1 with 65535
zeroes following).  A(6) is 2**65536 binary digits long, and cannot be
represented by the memory of the entire universe.


The Union Find data structure is not a universal set implementation, but can
tell you if two objects are in the same set, in different sets, or you can
combine two sets.
ufset.find(obja) == ufset.find(objb)
ufset.find(obja) != ufset.find(objb)
ufset.union(obja, objb)


This algorithm and data structure are primarily used for Kruskal's Minimum
Spanning Tree algorithm for graphs, but other uses have been found.



Originally by Josiah Carlson on August 12, 2003 
'''

__author__ = "bigfatnoob"

from collections import defaultdict


class UnionFind:
  def __init__(self, objects=None):
    """
    Create an empty union find data structure.
    """
    self.num_weights = {}
    self.parent_pointers = {}
    self.num_to_objects = {}
    self.objects_to_num = {}
    self.__repr__ = self.__str__
    if objects:
      self.insert_all(objects)

  def insert_all(self, objects):
    """
    Insert a sequence of objects into the structure.  All must be Python hashable.
    """
    for obj in objects:
      self.find(obj)

  def find(self, obj):
    """
    Find the root of the set that an object is in.
    If the object was not known, will make it known, and it becomes its own set.
    Object must be Python hashable.
    """
    if obj not in self.objects_to_num:
      obj_num = len(self.objects_to_num)
      self.num_weights[obj_num] = 1
      self.objects_to_num[obj] = obj_num
      self.num_to_objects[obj_num] = obj
      self.parent_pointers[obj_num] = obj_num
      return obj
    stk = [self.objects_to_num[obj]]
    par = self.parent_pointers[stk[-1]]
    while par != stk[-1]:
      stk.append(par)
      par = self.parent_pointers[par]
    for i in stk:
      self.parent_pointers[i] = par
    return self.num_to_objects[par]

  def union(self, object1, object2):
    """
    Combine the sets that contain the two objects given.
    Both objects must be Python hashable.
    If either or both objects are unknown, will make them known, and combine them.
    :param object1:
    :param object2:
    :return:
    """
    o1p = self.find(object1)
    o2p = self.find(object2)
    if o1p != o2p:
      on1 = self.objects_to_num[o1p]
      on2 = self.objects_to_num[o2p]
      w1 = self.num_weights[on1]
      w2 = self.num_weights[on2]
      if w1 < w2:
        o1p, o2p, on1, on2, w1, w2 = o2p, o1p, on2, on1, w2, w1
      self.num_weights[on1] = w1+w2
      del self.num_weights[on2]
      self.parent_pointers[on2] = on1

  def get_disjoint_sets(self):
    """
    Return set of disjoint sets
    :return: A dictionary of
    """
    clusters = defaultdict(list)
    for obj_num, cluster_num in self.parent_pointers.items():
      clusters[cluster_num].append(self.num_to_objects[obj_num])
    return clusters

  def __str__(self):
    """
    Included for testing purposes only.
    All information needed from the union find data structure can be attained
    using find.
    """
    sets = {}
    for i in xrange(len(self.objects_to_num)):
      sets[i] = []
    for i in self.objects_to_num:
      sets[self.objects_to_num[self.find(i)]].append(i)
    out = []
    for i in sets.itervalues():
      if i:
        out.append(repr(i))
    return ', '.join(out)


def _test():
  class Node:
    def __init__(self, val):
      self.val = val

  def __repr__(self):
    return str(self.val)

  def __str__(self):
    return str(self.val)
  nodes = [Node(1), Node(2), Node(3), Node(4), Node(5)]
  uf = UnionFind()
  uf.insert_all(nodes)
  uf.union(nodes[0], nodes[1])
  uf.union(nodes[3], nodes[4])
  print(uf.get_disjoint_sets())


if __name__ == "__main__":
  _test()

