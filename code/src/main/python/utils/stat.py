from __future__ import print_function, division
import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from utils import lib
import numpy as np


class Stat(lib.O):
  def __init__(self, arr, **kwargs):
    lib.O.__init__(self, **kwargs)
    self.arr = arr

  def max(self):
    return np.max(self.arr)

  def min(self):
    return np.min(self.arr)

  def mean(self):
    return np.asscalar(np.mean(self.arr))

  def median(self):
    return np.asscalar(np.median(self.arr))

  def std(self):
    return np.asscalar(np.std(self.arr))

  def iqr(self):
    [q75, q25] = np.percentile(self.arr, [75, 25])
    return q75 - q25

  def size(self):
    return len(self.arr)

  def report(self):
    return "\n".join(["```",
                      "\n".join(["%10s : %0.4f" % ("Min", self.min()),
                                 "%10s : %0.4f" % ("Mean", self.mean()),
                                 "%10s : %0.4f" % ("Median", self.median()),
                                 "%10s : %0.4f" % ("Max", self.max()),
                                 "%10s : %0.4f" % ("Std. Dev.", self.std()),
                                 "%10s : %0.4f" % ("IQR", self.iqr()),
                                 "%10s : %d" % ("Size", self.size())]),
                      "```"])
