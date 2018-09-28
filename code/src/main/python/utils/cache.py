from __future__ import print_function, division
import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import cPickle as cPkl
import json


def read_file(file_name):
  """
  Name of the file.
  :param file_name:
  :return:
  """
  with open(file_name) as f:
    return f.read()


def write_file(file_name, content):
  """
  Writing to the file
  :param file_name: Name of the file
  :param content: Content of the file
  :return:
  """
  splits = file_name.rsplit(os.path.sep, 1)
  if len(splits) > 1:
    mkdir(splits[0])
  with open(file_name, "wb") as f:
    f.write(content)


def load_pickle(file_name, verbose=False):
  """
  :return: Content of file_name
  """
  if not file_exists(file_name):
    if verbose:
      print("File %s does not exist" % file_name)
    return None
  try:
    with open(file_name) as f:
      return cPkl.load(f)
  except Exception:
    if verbose:
      print("Exception while loading file" % file_name)
    return None


def save_pickle(file_name, obj):
  """
  Save obj in file_name
  :param file_name:
  :param obj:
  :return:
  """
  splits = file_name.rsplit(os.path.sep, 1)
  if len(splits) > 1:
    mkdir(splits[0])
  with open(file_name, "wb") as f:
    cPkl.dump(obj, f, cPkl.HIGHEST_PROTOCOL)


def file_exists(file_name):
  """
  Check if file or folder exists
  :param file_name: Path of the file
  :return: True/False
  """
  return os.path.exists(file_name)


def mkdir(directory):
  """
  Create Directory if it does not exist
  """
  if not os.path.exists(directory):
    try:
      os.makedirs(directory)
    except OSError as e:
      if e.errno != os.errno.EEXIST:
        raise


def list_dir(directory, is_absolute=True):
  """
  List file names in directory
  :param directory: Path of directory
  :param is_absolute: If true returns complete path, else returns just the file/folder name
  :return: List of file/folder names
  """
  return [os.path.join((directory, f)) if is_absolute else f for f in os.listdir(directory)]


def load_json(file_name):
  """
  Read json from file name.
  :param file_name:
  :return:
  """
  try:
    return json.loads(read_file(file_name))
  except ValueError, e:
    print(e)
    return {}


def get_file_name(file_path):
  """
  Return name of the file from the path
  :param file_path: Path of the file
  :return: Name of the file
  """
  return file_path.rsplit(os.path.sep, 1)[-1].split(".", 1)[0]