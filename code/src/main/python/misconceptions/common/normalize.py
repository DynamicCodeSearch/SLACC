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


if __name__ == "__main__":
  normalize()
