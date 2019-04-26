import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


from misconceptions.common import mongo_driver, props, differences


def fetch_differences(limit=None):
  store = mongo_driver.MongoStore(props.DATASET)
  diff_records = store.load_differences(limit=limit)
  for diff_record in diff_records:
    # del diff_record["diff"]
    # print(diff_record)
    # exit()
    diffs = []
    for d in diff_record["diff"]:
      diff = differences.DiffMeta.from_dict(d)

      diffs.append(diff)
    summarize_diffs(diffs)


def summarize_diffs(diffs):
  # print(diffs)
  # exit()
  pass

if __name__ == "__main__":
  fetch_differences(10)
