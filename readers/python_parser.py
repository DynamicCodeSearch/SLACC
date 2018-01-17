from __future__ import print_function, division
import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import csv
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
  if destination_path[-1] == "/":
    destination_file = "%s%s.pkl" % (destination_path, name)
  else:
    destination_file = "%s/%s.pkl" % (destination_path, name)
  if cache.file_exists(destination_file):
    logger.info("%s file exists" % destination_file)
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
        # print(row['content'])
        errors += 1
      if cnt % 100 == 0:
        logger.info("Processed: %d / %d. Errors = %d" % (cnt, row_count, errors))
  cache.save(destination_file, func_objects)
  logger.info("Parsed Files. Errors = %d / %d" % (errors, cnt))
  logger.info("%s file saved" % destination_file)


def validate(file_name):
  data = cache.load(file_name)
  nones = 0
  for func_object in data:
    if func_object['doc_string'] is None:
      nones += 1
  print("%d in %d" % (nones, len(data)))


def parse_files(folder, destination_path, n_jobs):

  Parallel(n_jobs=n_jobs)(delayed(parse_file)(file_name, destination_path)
                          for file_name in cache.list_files(folder, is_relative=False))


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
