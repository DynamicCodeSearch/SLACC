from __future__ import print_function, division
import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


class O:
  def __init__(self, **d):
    """
    Base class. All classes must extend this.
    :param d: kwargs for object
    """
    self.has().update(**d)

  def has(self):
    """
    Return dictionary for object
    :return:
    """
    return self.__dict__

  def update(self, **d):
    """
    Update kwargs of dictionary
    :param d: kwargs to be updated.
    :return: Instance of object
    """
    self.has().update(d)
    return self

  def __repr__(self):
    """
    Represent as string
    :return:
    """
    show = [':%s %s' % (k, self.has()[k])
            for k in sorted(self.has().keys())
            if k[0] is not "_"]
    txt = ' '.join(show)
    if len(txt) > 60:
      show = map(lambda x: '\t' + x + '\n', show)
    return '{' + ' '.join(show) + '}'

  def __getitem__(self, key):
    """
    Retrieve item from dictionary.
    :param key: Key to be retrieved
    :return: Value at key. Will throw error if key does not exist
    """
    return self.has().get(key)

  def __setitem__(self, key, value):
    """
    Set value in dictionary.
    :param key: Key to be set
    :param value: Value at key
    """
    self.has()[key] = value
