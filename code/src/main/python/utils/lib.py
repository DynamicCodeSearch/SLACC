import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import properties

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


class O(object):
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


def is_int(string):
  """
  Check if string is an integer
  :param string:
  :return: True or false
  """
  try:
    int(string)
    return True
  except ValueError:
    return False


def get_dataset_functions_results_folder(dataset):
  """
  Return the path of folder containing the function results for the dataset
  :param dataset: Name of dataset
  :return: Path
  """
  return properties.FUNCTIONS_RESULTS_FOLDER % dataset


def get_dataset_meta_results_folder(dataset):
  """
  Return the path of folder containing the function meta data for the dataset
  :param dataset: Name of dataset
  :return: Path
  """
  return properties.FUNCTIONS_META_FOLDER % dataset


def get_dataset_arg_index(dataset):
  """
  Return the path of index json containing the arguments for the dataset
  :param dataset: Name of dataset
  :return: Path
  """
  return properties.ARGUMENTS_INDEX_JSON % dataset


def get_dataset_args_folder(dataset):
  """
  Return the path of folder containing the arguments for the dataset
  :param dataset: Name of dataset
  :return: Path
  """
  return properties.ARGUMENTS_FOLDER % dataset


def get_clusters_folder(dataset):
  """
  Return the path of folder containing the clusters for the dataset
  :param dataset: Name of dataset
  :return: Path
  """
  return properties.CLUSTERS_FOLDER % dataset

