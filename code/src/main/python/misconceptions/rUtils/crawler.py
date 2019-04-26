import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import json
import csv
from collections import Counter, OrderedDict
import rpy2.robjects as robjects

import matplotlib.pyplot as plt
from utils import cache, logger
from misconceptions.rUtils import parser, functions
from misconceptions.common import props, mongo_driver


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))
R_NOTEBOOKS_HOME = "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/R/IRNbs"
IRNB_CSV = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/src/main/python/expt/irnb.tsv"
PARSER = parser.DataFrameParser()


def convert_notebook(notebook_path, force=False):
  write_folder = cache.get_parent_folder(notebook_path)
  file_name = cache.get_file_name(notebook_path)
  write_file = os.path.join(write_folder, "%s.%s" % (file_name, props.TYPE_R))
  if not force and cache.file_exists(write_file):
    LOGGER.info("'%s' already converted. Moving on ... " % file_name)
    return
  else:
    LOGGER.info("Converting filename '%s' ... " % file_name)
  source_code_lines = []
  with open(notebook_path) as fh:
    json_obj = json.load(fh)
    cells = json_obj['cells']
    for cell in cells:
      if cell['cell_type'] == 'code' and cell['source']:
        source_code_lines += cell['source']
  source_code = "\n".join(source_code_lines)
  with open(write_file, 'w+') as fh:
    fh.writelines(source_code.encode('utf-8'))
  if not functions.r_compile(write_file, del_compiled=True):
    cache.delete_file(write_file)
    return False
  return True


def convert_R_notebooks(force=False):
  irnb_files = cache.list_files_with_extension(R_NOTEBOOKS_HOME, ".irnb", check_nest=True, is_absolute=True)
  n_count = len(irnb_files)
  valids = 0
  for i, file_name in enumerate(irnb_files):
    LOGGER.info("Processing %d / %d ... " % (i+1, n_count))
    if convert_notebook(file_name, force=force):
      valids += 1
  LOGGER.info("Valid Files: %d / %d" % (valids, n_count))


def get_converted_files():
  return cache.list_files_with_extension(R_NOTEBOOKS_HOME, ".R", check_nest=True, is_absolute=True)


def runner(force=False):
  store = mongo_driver.MongoStore(props.DATASET)
  if force:
    store.delete_file_stmts(props.TYPE_R)
  r_files = get_converted_files()
  for i, r_file in enumerate(r_files):
    file_name = cache.get_file_name(r_file)
    if store.load_stmts_for_file_name(r_file):
      LOGGER.info("Processed %s. Moving on ... " % file_name)
      continue
    LOGGER.info("Processing %d / %d ... " % (i + 1, len(r_files)))
    LOGGER.info("Processing %s ... " % file_name)
    lines = PARSER.parse_file(r_file)
    store.store_file_stmts(r_file, lines, props.TYPE_R)


def dump_extracted_to_csv():
  store = mongo_driver.MongoStore(props.DATASET)
  docs = store.load_file_stmts(props.TYPE_R)
  stmt_counter = Counter()
  stmt_file_map = {}
  for i, doc in enumerate(docs):
    file_name = doc['file_name']
    LOGGER.info("Processing %d / %d ... " % (i + 1, docs.count()))
    for stmt in doc['snippets']:
      stmt_counter[stmt] = stmt_counter.get(stmt, 0) + 1
      file_names = stmt_file_map.get(stmt, set())
      file_names.add(file_name)
      stmt_file_map[stmt] = file_names
  with open(IRNB_CSV, "wb") as csv_file:
    writer = csv.writer(csv_file, delimiter='\t')
    writer.writerow(["Statement", "Count", "# unique files"])
    for stmt, count in stmt_counter.most_common():
      writer.writerow([unicode(stmt).encode("utf-8"), count, len(stmt_file_map[stmt])])


def get_stmt_counts(limit=None):
  store = mongo_driver.MongoStore(props.DATASET)
  docs = store.load_file_stmts(props.TYPE_R)
  stmt_counter = Counter()
  for i, doc in enumerate(docs):
    for stmt in doc['snippets']:
      stmt_counter[stmt] = stmt_counter.get(stmt, 0) + 1
  stmts = OrderedDict()
  for stmt, count in stmt_counter.most_common(limit):
    stmts[stmt] = count
  return stmts


def _test():
  # convert_notebook("/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/R/IRNbs/abahl88/titanic-disaster-survival-analysis/titanic-disaster-survival-analysis.R")
  lines = PARSER.parse_file("/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/R/IRNbs/abahl88/titanic-disaster-survival-analysis/titanic-disaster-survival-analysis.R")
  for line in lines:
    print(line)
  print(len(lines))


def _test_compile():
  # print(functions.r_compile("/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/R/IRNbs/abahl88/titanic-disaster-survival-analysis/titanic-disaster-survival-analysis.R"))
  print(functions.r_compile("/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/R/IRNbs/edouardmalet/a-journey-through-titanic/a-journey-through-titanic.R"))


if __name__ == "__main__":
  # _test_compile()
  # convert_R_notebooks(force=True)
  runner(force=True)
  dump_extracted_to_csv()
