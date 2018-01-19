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

LOG_LEVEL = logging.INFO
logger = get_logger(__name__, LOG_LEVEL)
csv.field_size_limit(sys.maxsize)


def handled_csv_reader(csv_reader):
  while True:
    try:
      yield next(csv_reader)
    except csv.Error:
      pass
    continue
  return


def get_header_and_row_count(file_name):
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


def collect_statistics(file_name, destination_path):
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
  Parallel(n_jobs=n_jobs)(delayed(collect_statistics)(file_name, destination_path)
                          for file_name in sorted(cache.list_files(folder, is_relative=False)))


def get_function_stats(function):
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


def validate(file_name):
  data = cache.load(file_name)
  nones = 0
  for func_object in data:
    if func_object['doc_string'] is None:
      nones += 1
  print("%d in %d" % (nones, len(data)))


def parse_files(folder, destination_path, n_jobs):
  Parallel(n_jobs=n_jobs)(delayed(parse_file)(file_name, destination_path)
                          for file_name in sorted(cache.list_files(folder, is_relative=False)))


def _parse_files():
  folder = "data/pyfiles_dump/csv"
  destination_path = "data/pyfiles_dump/functions/"
  n_jobs = 1
  args = sys.argv
  if len(args) >= 2 and lib.is_int(args[1]):
    n_jobs = int(args[1])
  parse_files(folder, destination_path, n_jobs)


if __name__ == "__main__":
  # parse_file("data/pyfiles_dump/csv/000000000002.csv", "data/pyfiles_dump/functions/")
  # validate("data/pyfiles_dump/functions/000000000000.pkl")
  _parse_files()
  # collect_statistics("data/pyfiles_dump/functions/000000000000.pkl", "data/pyfiles_dump/stats")

