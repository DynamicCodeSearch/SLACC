import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import cPickle as cPkl
import json
import logger
import shutil


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


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


def delete_file(path):
  """
  Delete a file
  :param path: Path of the file
  """
  if file_exists(path):
    os.remove(path)


def delete_folder(path):
  """
  Delete a folder
  :param path:  Path of folder
  """
  if file_exists(path):
    shutil.rmtree(path)


def mkdir(directory):
  """
  Create Directory if it does not exist
  """
  if not file_exists(directory):
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
    LOGGER.info("ERROR while processing file: %s", file_name)
    LOGGER.exception(e, exc_info=True)
    # print(file_name)
    return {}


def get_file_name(file_path):
  """
  Return name of the file from the path
  :param file_path: Path of the file
  :return: Name of the file
  """
  return file_path.rsplit(os.path.sep, 1)[-1].split(".", 1)[0]


def mk_package(path):
  """
  Make the folder in the path a python package
  :param path: Path of the folder
  """
  if not file_exists(path):
    try:
      os.makedirs(path)
      init_path = os.path.join(path, "__init__.py")
      write_file(init_path, "")
    except OSError as e:
      if e.errno != os.errno.EEXIST:
        raise


def is_valid_python_file(path):
  try:
    with open(path, 'r') as f:
      compile(f.read(), path, 'exec')
      return True
  except Exception as e:
    return False
