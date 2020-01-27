import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


from store import mongo_driver


def clear_db(dataset):
  db = mongo_driver.get_dataset_db(dataset)
  if db is None:
    return
  mongo_driver.get_client().drop_database(dataset)


def create_db(dataset):
  db = mongo_driver.get_dataset_db(dataset)
  collection = db.get_collection("test_collection")
  res = collection.insert_one({"name": "Hello World!"})


if __name__ == "__main__":
  args = sys.argv
  if len(args) < 2:
    print("Use: python store/init_db.py <dataset>")
    exit(0)
  else:
    clear_db(args[1])
    create_db(args[1])
