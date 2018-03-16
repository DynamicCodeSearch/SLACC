from __future__ import print_function, division
import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


import csv
import cPickle as cPkl


def load(file_name, verbose=False):
  """
  :return: Content of file_name
  """
  if not file_exists(file_name):
    if verbose:
      print("File %s does not exist" % file_name)
    return None
  with open(file_name) as f:
    try:
      return cPkl.load(f)
    except Exception as e:
      if verbose:
        print("Exception while loading file" % file_name)
      return None


def save(file_name, obj):
  """
  Save obj in file_name
  :param file_name:
  :param obj:
  :return:
  """
  splits = file_name.rsplit("/", 1)
  if len(splits) > 1:
    mkdir(splits[0])
  with open(file_name, "wb") as f:
    cPkl.dump(obj, f, cPkl.HIGHEST_PROTOCOL)


def save_text(file_name, text):
  """
  Save text in file_name
  :param file_name: Name of File
  :param text: Text to be saved
  """
  splits = file_name.rsplit("/", 1)
  if len(splits) > 1:
    mkdir(splits[0])
  with open(file_name, "wb") as f:
    f.write(text)


def delete(file_name):
  """
  Delete file if it exists
  :param file_name:
  :return:
  """
  if file_name and file_exists(file_name):
    try:
      os.remove(file_name)
    except OSError, e:
      if e.errno != os.errno.ENOENT:
        raise


def create_file_path(directory, file_name, ext=None):
  """
  Concatenate file name and directory to
  create complete file path
  :param directory: Name of directory
  :param file_name: Name of file
  :param ext: Extension fo file
  :return: Concatenated File Name
  """
  mkdir(directory)
  fmt = "%s%s" if directory[-1] == "/" else "%s/%s"
  if ext is not None:
    fmt += ext
  return fmt % (directory, file_name)


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
    except OSError, e:
      if e.errno != os.errno.EEXIST:
        raise


def list_files(directory, is_relative=False):
  """
  List files/folders in the directory
  :param directory: Path of the directory
  :param is_relative: If true returns relative name else absolute name
  :return: [List of file/folder names]
  """
  if not os.path.exists(directory):
    return []
  if directory[-1] == "/":
    directory = directory[:-1]
  prefix = "%s/" % directory if not is_relative else ""
  return ["%s%s" % (prefix, f) for f in os.listdir(directory)]


def write_csv(file_name, rows, delimiter=',', quotechar='"'):
  """
  Write a csv
  :param file_name: Name of the file
  :param rows: List of lists indicating cells of the csv
  :param delimiter: Separator character
  :param quotechar: Quote character to escape
  :return:
  """
  splits = file_name.rsplit("/", 1)
  if len(splits) > 1:
    mkdir(splits[0])
  with open(file_name, "wb") as csv_file:
    result_writer = csv.writer(csv_file, delimiter=delimiter, quotechar=quotechar, quoting=csv.QUOTE_MINIMAL)
    for row in rows:
      result_writer.writerow(row)


def write_markdown(file_name, rows, header=True):
  """
  Write as markdown
  :param file_name: Name of the file
  :param rows: List of lists indicating cells of the csv
  :param header: If header row is included
  :return:
  """
  lines = []
  for row in rows:
    lines.append("| %s |" % " | ".join(map(str, row)))
  if header:
    separator = "| %s |" % " | ".join(["------"] * len(rows[0]))
    lines = lines[:1] + [separator] + lines[1:]
  save(file_name, "\n".join(lines))
