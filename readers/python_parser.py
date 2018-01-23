from __future__ import print_function, division
import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import csv
import re
import ast, asttokens
import logging
from utils.logger import get_logger
from utils import cache, lib
from joblib import Parallel, delayed
import numpy as np

LOG_LEVEL = logging.INFO
logger = get_logger(__name__, LOG_LEVEL)
csv.field_size_limit(sys.maxsize)


def handled_csv_reader(csv_reader):
  """
  A modified version of CSV reader with handles CSV formatting error
  :param csv_reader: CSV reader
  :return:
  """
  while True:
    try:
      yield next(csv_reader)
    except csv.Error:
      pass
    continue
  return


def get_header_and_row_count(file_name):
  """
  Access header and get number of rows
  in the csv file
  :param file_name: Name of csv file
  :return: (Header, Number of rows in csv file)
  """
  with open(file_name, "rb") as csv_file:
    header = None
    header_reader = handled_csv_reader(csv.reader(csv_file))
    cnt = 0
    for row in header_reader:
      if header is None:
        header = row
      else:
        cnt += 1
    return header, cnt


def parse_file(file_name, destination_path):
  """
  Parse csv file, extract functions and save into a pkl.
  :param file_name: Name of the file.
  :param destination_path: Folder where extracted file
   is saved
  """
  name = file_name.rsplit("/", 1)[-1].split(".")[0]
  destination_file = cache.create_file_path(destination_path, name, ext=".pkl")
  temp_file = cache.create_file_path(destination_path, name, ext=".tmp")
  if cache.file_exists(destination_file):
    logger.info("%s file exists" % destination_file)
    return
  if cache.file_exists(temp_file):
    logger.info("%s file being processed" % destination_file)
    return
  cache.save(temp_file, {"Processing": True})
  header, row_count = get_header_and_row_count(file_name)
  with open(file_name, "rb") as csv_file:
    header_reader = handled_csv_reader(csv.reader(csv_file))
    for _ in header_reader: break
    reader = handled_csv_reader(csv.DictReader(csv_file, header))
    cnt = 0
    errors = 0
    func_objects = []
    for row in reader:
      cnt += 1
      try:
        ast_tokens = asttokens.ASTTokens(row['content'], parse=True)
        for node in ast.walk(ast_tokens.tree):
          if isinstance(node, ast.FunctionDef):
            func_object = {
                "id": row['id'],
                "path": row['path'],
                "doc_string": ast.get_docstring(node),
                "body": ast_tokens.get_text(node)
            }
            func_objects.append(func_object)
      except Exception:
        errors += 1
      if cnt % 100 == 0:
        logger.info("Index: %s; Processed: %d / %d. Errors = %d" % (name[-4:], cnt, row_count, errors))
  cache.save(destination_file, func_objects)
  cache.delete(temp_file)
  logger.info("Index: %s; Parsed Files. Errors = %d / %d" % (name[-4:], errors, cnt))
  logger.info("%s file saved" % destination_file)


def parse_files(folder, destination_path, n_jobs):
  """
  Parse all csv files in folder in a parallel manner
  :param folder: Path of source of folder
  :param destination_path: Path of destination folder
  :param n_jobs: Number of jobs to run in parallel
  """
  Parallel(n_jobs=n_jobs)(delayed(parse_file)(file_name, destination_path)
                          for file_name in sorted(cache.list_files(folder, is_relative=False)))


def _parse_files():
  """
  Runner for parse_files function.
  :return:
  """
  folder = "data/pyfiles_dump/csv"
  destination_path = "data/pyfiles_dump/functions/"
  n_jobs = 1
  args = sys.argv
  if len(args) >= 2 and lib.is_int(args[1]):
    n_jobs = int(args[1])
  parse_files(folder, destination_path, n_jobs)


def collect_statistics(file_name, destination_path):
  """
  Collect statistics for each pkl file.
  :param file_name: Name of .pkl file
  :param destination_path: Destination folder for statistics file
  """
  if file_name[-4:] != ".pkl":
    logger.info("INVALID FILE: %s" % file_name)
    return
  name = file_name.rsplit("/", 1)[-1].split(".")[0]
  destination_file = cache.create_file_path(destination_path, name, ext=".pkl")
  temp_file = cache.create_file_path(destination_path, name, ext=".tmp")
  if cache.file_exists(destination_file):
    logger.info("%s file exists" % destination_file)
    return
  if cache.file_exists(temp_file):
    logger.info("%s file being processed" % destination_file)
    return
  functions = cache.load(file_name)
  cache.save(temp_file, {"Processing": True})
  stats = []
  cnt = 0
  errors = 0
  n_functions = len(functions)
  for function in functions:
    cnt += 1
    stat = get_function_stats(function)
    if stat is not None:
      stats.append(stat)
    else:
      errors += 1
    if cnt % 10000 == 0:
      logger.info("Index: %s; Processed: %d / %d. Errors: %d" % (name[-4:], cnt, n_functions, errors))
  cache.delete(temp_file)
  cache.save(destination_file, stats)
  logger.info("Index: %s; Parsed all functions. Errors: %d" % (name[-4:], errors))


def collect_stats_for_all(folder, destination_path, n_jobs):
  """
  Collect stats for all pkl files in folder in parallel
  :param folder: Path of source folder
  :param destination_path: Path of destination folder
  :param n_jobs: Number of parallel jobs to be run.
  """
  Parallel(n_jobs=n_jobs)(delayed(collect_statistics)(file_name, destination_path)
                          for file_name in sorted(cache.list_files(folder, is_relative=False)))


def get_function_stats(function):
  """
  Get stats for a function dictionary object
  :param function: Dictionary object. Contains 'body' and 'doc_string'
  :return: {"comment_length": comment_length, "body_length": body_length}
  """
  body = function['body']
  annotations = r'@.+'
  if body.strip()[0] == '@':
    body = re.sub(annotations, '', function['body'], count=1)
  body = body.strip()
  # try:
  #   tokenized = asttokens.ASTTokens(body, parse=True)
  # except Exception:
  #   return None
  comment = function['doc_string']
  comment_length = 0
  if comment is not None:
    comment_length = sum([1 if len(line.strip()) > 0 else 0 for line in comment.split("\n")])
  body_length = sum([1 if len(line.strip()) > 0 else 0 for line in body.split("\n")])
  body_length -= comment_length + 1
  if body[0] == "@":
    body_length -= 1
  # n_args = 0
  # for node in ast.walk(tokenized.tree):
  #   if isinstance(node, ast.FunctionDef):
  #     args = tokenized.get_text(node.args).strip()
  #     if len(args) > 0:
  #       n_args = len(args.split(","))
  stats = {
      "comment_length": comment_length,
      "body_length": body_length,
      # "n_args": n_args
  }
  return stats


def aggregate(folder, destination):
  """
  Aggregate statistics for all files in folder
  :param folder: Path of source folder
  :param destination: Path of destination folder
  :return: {
      "comment_length": [comment_lengths],
      "body_length": [body_lengths]
  }
  """
  data = {
      "comment_length": [],
      "body_length": []
  }
  for file_name in cache.list_files(folder, is_relative=False):
    stats = cache.load(file_name)
    for stat in stats:
      data["comment_length"].append(stat["comment_length"])
      data["body_length"].append(stat["body_length"])
    print(file_name)
  cache.save(destination, data)


def summarize(file_name):
  """
  Summarize aggregated statistics
  :param file_name: Source of aggregated files
  """
  stats = cache.load(file_name)
  comments = np.array(stats['comment_length'])
  bodies = np.array(stats['body_length'])
  print("Num Functions = %d" % len(comments))
  print("Mean Size of functions = %d" % np.average(bodies))
  print("Std Dev Size of functions = %d" % np.std(bodies))
  funcs_with_comments = comments[np.where(comments > 0)[0]]
  print("Functions with comments = %d" % len(funcs_with_comments))
  print("Mean Size of comments = %d" % np.average(funcs_with_comments))
  print("Std Dev Size of comments = %d" % np.std(funcs_with_comments))


def validate(file_name):
  """
  Functions in file name that contains comments
  :param file_name: Path of source pkl file
  """
  data = cache.load(file_name)
  nones = 0
  for func_object in data:
    if func_object['doc_string'] is None:
      nones += 1
  print("%d in %d" % (nones, len(data)))


def shrink_csv_file(file_name, write_folder, size):
  """
  Reduce number of rows in csv file
  :param file_name: Name of csv file
  :param write_folder: Destination folder to write
  :param size: Number of rows to be retained
  """
  name = file_name.rsplit("/", 1)[-1].split(".")[0]
  write_file = cache.create_file_path(write_folder, name, ".csv")
  if cache.file_exists(write_file):
    logger.info("%s is already processed" % name)
    return
  logger.info("%s file being processed" % name)
  header, row_count = get_header_and_row_count(file_name)
  logger.info("Computed header and row size for %s" % name)
  with open(file_name, "rb") as csv_file:
    header_reader = handled_csv_reader(csv.reader(csv_file))
    for _ in header_reader: break
    reader = handled_csv_reader(csv.DictReader(csv_file, header))
    func_objects = []
    for row in reader:
      func_objects.append(row)
      if len(func_objects) == size: break
  with open(write_file, "wb") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=header)
    writer.writeheader()
    for row in func_objects:
      writer.writerow(row)
  logger.info("Saved first %d rows of %s" % (size, name))


def shrink_csv_files_in_folder(folder, write_folder, size, n_jobs):
  """
  Reduce number of rows in csv files in a folder in parallel manner
  :param folder: Path of source folder
  :param write_folder: Path of destination folder
  :param size: Number of rows to be retained
  :param n_jobs: Number of jobs to run in parallel
  :return:
  """
  Parallel(n_jobs=n_jobs)(delayed(shrink_csv_file)(file_name, write_folder, size)
                          for file_name in sorted(cache.list_files(folder, is_relative=False)))


def commented_functions(file_name, write_folder, size=None):
  """
  Save commented functions from file. Can be used for text analysis
  :param file_name: Name of .pkl file
  :param write_folder: Path of destination folder
  :param size: Number of rows to be retained
  :return: Number of jobs to run in parallel
  """
  name = file_name.rsplit("/", 1)[-1].split(".")[0]
  write_file = cache.create_file_path(write_folder, name, ".pkl")
  if cache.file_exists(write_file):
    logger.info("%s is already processed" % name)
    return
  logger.info("%s file being processed" % name)
  data = cache.load(file_name)
  valid_functions = []
  if size is None:
    size = len(data)
  count = 0
  for func_object in data:
    count += 1
    if func_object['doc_string'] is not None:
      valid_functions.append(func_object)
    if len(valid_functions) == size:
      break
  cache.save(write_file, valid_functions)
  logger.info("%d / %d valid functions in %s" % (len(valid_functions), count, name))


def commented_functions_in_folder(folder, write_folder, size=None, n_jobs=1):
  """
  Save commented functions from pkl files in a folder in parallel manner
  :param folder: Path of source folder
  :param write_folder: Path of destination folder
  :param size: Number of rows to be retained
  :param n_jobs: Number of jobs to run in parallel
  :return:
  """
  Parallel(n_jobs=n_jobs)(delayed(commented_functions)(file_name, write_folder, size)
                          for file_name in sorted(cache.list_files(folder, is_relative=False)))


if __name__ == "__main__":
  # parse_file("data/pyfiles_dump/csv/000000000002.csv", "data/pyfiles_dump/functions/")
  # validate("data/pyfiles_dump/functions/000000000000.pkl")
  # _parse_files()
  # collect_statistics("data/pyfiles_dump/functions/000000000000.pkl", "data/pyfiles_dump/stats")
  # aggregate("data/pyfiles_dump/stats/indeps", "data/pyfiles_dump/stats/all.pkl")
  # summarize("data/pyfiles_dump/stats/all.pkl")
  # shrink_csv_files_in_folder("data/pyfiles_dump/csv/", "data/pyfiles_dump/csv_mini", 1000, 2)
  commented_functions_in_folder("data/pyfiles_dump/functions/", "data/pyfiles_dump/commented_functions", None, 2)

