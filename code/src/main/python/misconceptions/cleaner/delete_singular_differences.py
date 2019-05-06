import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


from utils import logger
from misconceptions.common import mongo_driver, props, compare


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def delete_single_output_stmts(limit=0, log_interval=100):
  store = mongo_driver.MongoStore(props.DATASET)
  stmts = store.load_stmts(language=None, is_valid=True, has_output=True,
                           limit=limit).values()
  valids = {}
  for i, stmt in enumerate(stmts):
    if i % log_interval == 0:
      LOGGER.info("Processing statement %d/%d ... " % (i, len(stmts)))
    meta = stmt.get("meta", {})
    stmt_valids = set()
    for key, validity in meta.items():
      if validity:
        stmt_valids.add(mongo_driver.mongo_de_escape(key))
    if len(stmt_valids) > 0:
      valids[stmt["_id"]] = stmt_valids
  LOGGER.info("Non singular output stmts: %d/%d" % (len(valids), len(stmts)))
  differences = store.load_differences(projection={"_id": True, "r_id": True, "py_id": True,
                                                   "r_return": True, "py_return": True}, limit=limit)
  to_delete = []
  n_differences = differences.count()
  i = 0
  for diff in differences:
    i += 1
    if i % log_interval == 0:
      LOGGER.info("Processing differences: %d / %d" % (i, n_differences))
    r_id, py_id = diff["r_id"], diff["py_id"]
    if (r_id in valids) and (diff["r_return"] in valids[r_id]):
      to_delete.append(diff["_id"])
      continue
    if (py_id in valids) and (diff["py_return"] in valids[py_id]):
      to_delete.append(diff["_id"])
      continue
  LOGGER.info("Differences to delete: %d / %d" % (len(to_delete), differences.count()))
  for i, diff_id in enumerate(to_delete):
    if i % log_interval == 0:
      LOGGER.info("Deleting difference %d/%d ... " % (i, len(to_delete)))
    store.delete_difference(diff_id)


if __name__ == "__main__":
  delete_single_output_stmts()
