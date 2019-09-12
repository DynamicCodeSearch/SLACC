import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


from utils import logger
from misconceptions.common import mongo_driver, props, compare


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def get_single_output_stmts(language, limit=None, log_interval=100):
  store = mongo_driver.MongoStore(props.DATASET)
  mongo_stmts = store.load_stmts(language=language, is_valid=True, has_output=True, limit=limit, use_normalized=True).items()
  LOGGER.info("Fetched statements from mongo ... ")
  n_stmts = len(mongo_stmts)
  n_singular_output_stmts = 0
  for i, (key, mongo_stmt) in enumerate(mongo_stmts):
    do_log = (i + 1) % log_interval == 0
    if do_log:
      LOGGER.info("Processing %d / %d .... " % (i + 1, n_stmts))
    stmt = compare.Statement(mongo_id=mongo_stmt["_id"], snippet=mongo_stmt["snippet"],
                             variables=mongo_stmt["variables"], language=language,
                             outputs=compare.format_outputs(mongo_stmt["outputs"]))
    is_all_same = {}
    for ret_key in stmt.outputs.keys():
      is_all_same[ret_key] = stmt.outputs[ret_key].is_all_same
      if stmt.outputs[ret_key].is_all_same:
        n_singular_output_stmts += 1
    store.update_stmt(stmt.mongo_id, {"meta": is_all_same})
  LOGGER.info("Completed. Singular Output Statements = %d / %d" % (n_singular_output_stmts, n_stmts))


if __name__ == "__main__":
  get_single_output_stmts(language=None)
