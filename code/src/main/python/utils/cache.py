from __future__ import print_function, division
import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import pickle as c_pickle
import json
import openpyxl
from openpyxl.reader import excel
from utils import logger
import shutil


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def get_parent_folder(file_name):
  splits = file_name.rsplit(os.path.sep, 1)
  if len(splits) > 1:
    return splits[0]
  return None


def read_file(file_name):
  """
  Name of the file.
  :param file_name:
  :return:
  """
  with open(file_name, "r") as f:
    return f.read()


def write_file(file_name, content, mode='w'):
  """
  Writing to the file
  :param file_name: Name of the file
  :param content: Content of the file
  :param mode: Mode of the file
  :return:
  """
  parent = get_parent_folder(file_name)
  if parent:
    mkdir(parent)
  with open(file_name, mode) as f:
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
    with open(file_name, "r") as f:
      return c_pickle.load(f)
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
  parent = get_parent_folder(file_name)
  if parent:
    mkdir(parent)
  with open(file_name, "w") as f:
    c_pickle.dump(obj, f, c_pickle.HIGHEST_PROTOCOL)


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
  return [os.path.join(directory, f) if is_absolute else f for f in os.listdir(directory)]


def load_json(file_name):
  """
  Read json from file name.
  :param file_name:
  :return:
  """
  try:
    return json.loads(read_file(file_name))
  except ValueError as e:
    LOGGER.info("ERROR while processing file: %s", file_name)
    LOGGER.exception(e, exc_info=True)
    # print(file_name)
    return {}


def store_json(data, file_name, mode='w'):
  """
  Store json file
  :param data: Type of data
  :param file_name: Name of file
  :param mode: Mode of writing(w/wb)
  :return:
  """
  parent = get_parent_folder(file_name)
  if parent:
    mkdir(parent)
  with open(file_name, mode) as json_file:
    json.dump(data, json_file, default=lambda o: o.__dict__, indent=2)


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


def list_files(folder, check_nest=False, is_absolute=False, ignores=None):
  """
  List files in the folder
  :param folder: Path of the folder
  :param check_nest: If true walks through nested folders
  :param is_absolute: If true returns absolute path else return relative path
  :param ignores: List of file names to ignore
  :return: List of files
  """
  files = []
  for f in os.listdir(folder):
    child = os.path.join(folder, f)
    if os.path.isdir(child) and check_nest:
      child_files = list_files(child, check_nest=True, is_absolute=is_absolute, ignores=ignores)
      if child_files:
        files += child_files
    elif not os.path.isdir(child):
      if ignores and f in ignores:
        continue
      if is_absolute:
        files.append(child)
      else:
        files.append(f)
  return files


def list_files_with_extension(folder, extension, check_nest=False, is_absolute=False, ignores=None):
  """
  List file in the folder which match extension
  :param folder: Path of the folder
  :param extension: Extension of the file(Don't forget the ".")
  :param check_nest: If true walks through nested folders
  :param is_absolute: If true returns absolute path else return relative path
  :param ignores: List of file names to ignore
  :return: List of files
  """
  files = []
  for f in os.listdir(folder):
    child = os.path.join(folder, f)
    if os.path.isdir(child) and check_nest:
      child_files = list_files_with_extension(child, extension, check_nest=True, is_absolute=is_absolute, ignores=ignores)
      if child_files:
        files += child_files
    elif not os.path.isdir(child):
      if not child.endswith(extension) or (ignores and f in ignores): continue
      if is_absolute:
        files.append(child)
      else:
        files.append(f)
  return files


def read_excel(path, read_only=False):
  """
  Read excel file and return workbook object.
  Look up docs in https://www.datacamp.com/community/tutorials/python-excel-tutorial
  :param path: Path of the excel file
  :param read_only: If set to true, this would make the read faster and for better optimization
  :return: Workbook object
  """
  return openpyxl.load_workbook(path,  read_only=read_only)
