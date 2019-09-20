import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import csv
import nbformat
from nbconvert import PythonExporter
from collections import Counter, OrderedDict


from utils import cache, logger
from misconceptions.pdUtils import parser
from misconceptions.common import mongo_driver, props


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))
PYTHON_NOTEBOOKS_HOME = "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/python/IPythonNbs"
IPYTHON_CSV = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/src/main/python/expt/ipython.tsv"
PARSER = parser.DataFrameParser()


def convert_notebook(notebook_path):
  write_folder = cache.get_parent_folder(notebook_path)
  file_name = cache.get_file_name(notebook_path)
  write_file = os.path.join(write_folder, "%s.%s" % (file_name, props.TYPE_PYTHON))
  if cache.file_exists(write_file):
    LOGGER.info("'%s' already converted. Moving on ... " % file_name)
    return
  else:
    LOGGER.info("Converting filename '%s' ... " % file_name)
  with open(notebook_path) as fh:
    nb = nbformat.reads(fh.read(), nbformat.NO_CONVERT)
  exporter = PythonExporter()
  try:
    source, meta = exporter.from_notebook_node(nb)
  except nbformat.validator.NotebookValidationError:
    LOGGER.error("Validation error while converting '%s'." % notebook_path)
    return
  with open(write_file, 'w+') as fh:
    fh.writelines(source.encode('utf-8'))


def convert_python_notebooks():
  ipython_files = cache.list_files_with_extension(PYTHON_NOTEBOOKS_HOME, ".ipynb", check_nest=True, is_absolute=True)
  n_count = len(ipython_files)
  for i, file_name in enumerate(ipython_files):
    LOGGER.info("Processing %d / %d ... " % (i+1, n_count))
    convert_notebook(file_name)


def get_converted_files():
  return cache.list_files_with_extension(PYTHON_NOTEBOOKS_HOME, ".py", check_nest=True, is_absolute=True)


def runner(force=False):
  store = mongo_driver.MongoStore(props.DATASET)
  if force:
    store.delete_file_stmts(props.TYPE_PYTHON)
  py_files = get_converted_files()
  for i, py_file in enumerate(py_files):
    file_name = cache.get_file_name(py_file)
    if store.load_stmts_for_file_name(py_file):
      LOGGER.info("Processed %s. Moving on ... " % file_name)
      continue
    LOGGER.info("Processing %d / %d ... " % (i + 1, len(py_files)))
    LOGGER.info("Processing %s ... " % file_name)
    lines = PARSER.parse_file(py_file)
    store.store_file_stmts(py_file, lines, props.TYPE_PYTHON)


def dump_extracted_to_csv():
  store = mongo_driver.MongoStore(props.DATASET)
  docs = store.load_file_stmts(props.TYPE_PYTHON)
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
  with open(IPYTHON_CSV, "wb") as csv_file:
    writer = csv.writer(csv_file, delimiter='\t')
    writer.writerow(["Statement", "Count", "# unique files"])
    for stmt, count in stmt_counter.most_common():
      writer.writerow([unicode(stmt).encode("utf-8"), count, len(stmt_file_map[stmt])])


def get_stmt_counts(limit=None):
  store = mongo_driver.MongoStore(props.DATASET)
  docs = store.load_file_stmts(props.TYPE_PYTHON)
  stmt_counter = Counter()
  for i, doc in enumerate(docs):
    for stmt in doc['snippets']:
      stmt_counter[stmt] = stmt_counter.get(stmt, 0) + 1
  stmts = OrderedDict()
  for stmt, count in stmt_counter.most_common(limit):
    stmts[stmt] = count
  return stmts


def _test():
  x = "train_df.head()"
  stmts = get_stmt_counts(10)
  print(stmts)


if __name__ == "__main__":
  # convert_python_notebooks()
  # runner(False)
  # dump_extracted_to_csv()
  _test()
