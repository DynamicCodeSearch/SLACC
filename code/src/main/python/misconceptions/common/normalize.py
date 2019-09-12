import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


from misconceptions.common import mongo_driver, props, syntactic
from utils import lib, cache, logger


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def normalize(log_interval=100):
  store = mongo_driver.MongoStore(props.DATASET)
  LOGGER.info("Fetching statements ... ")
  cursor = store.load_raw_stmts()
  stmts = []
  for stmt in cursor:
    if not stmt.get('variables', None) or not stmt.get('outputs', None):
      continue
    stmts.append(stmt)
  del cursor
  LOGGER.info("Valid Statements: %d!" % len(stmts))
  for i, stmt in enumerate(stmts):
    if (i + 1) % log_interval == 0:
      LOGGER.info("Processing statement: %d/%d" % (i + 1, len(stmts)))
    stmt["snippet"] = syntactic.normalize(stmt)
    del stmt["_id"]
    store.store_normalized_stmt(stmt)


def create_normalized_stmt_file_map():
  store = mongo_driver.MongoStore(props.DATASET)
  LOGGER.info("Fetching Stmts .... ")
  valid_stmts = store.load_stmts(is_valid=True, has_output=True)
  LOGGER.info("Fetching File Stmts .... ")
  file_stmts = store.load_file_stmts()
  back_pointers = {}
  i, n_file_stmts = 0, file_stmts.count()
  for file_stmt in file_stmts:
    i += 1
    LOGGER.info("Processing file %d / %d ... " % (i, n_file_stmts))
    file_name = file_stmt['file_name'].split(props.PROJECTS_SRC)[-1].split("/", 2)[-1]
    language = file_stmt['language']
    for snippet in file_stmt['snippets']:
      if (snippet, language) not in valid_stmts:
        continue
      normalized_snippet = syntactic.normalize(valid_stmts[(snippet, language)])
      if normalized_snippet not in back_pointers:
        back_pointers[normalized_snippet] = {
          "language": language,
          "file_names": set()
        }
      back_pointers[normalized_snippet]["file_names"].add(file_name)
  LOGGER.info("Saving stmt to file pointers ... ")
  for snippet, back_pointer in back_pointers.items():
    back_pointer["file_names"] = list(back_pointer["file_names"])
    store.create_stmt_file_map(snippet, back_pointer)


if __name__ == "__main__":
  # normalize()
  create_normalized_stmt_file_map()
