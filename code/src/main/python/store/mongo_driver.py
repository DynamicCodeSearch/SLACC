import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


from pymongo import MongoClient
import socket

from utils import cache, logger


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))
__MONGO_CLIENT = None


def get_default_hostname():
  return socket.gethostname()


def get_hostname():
  mongo_home = os.environ.get("MONGO_HOME", None)
  if mongo_home:
    file_name = os.path.join(mongo_home, "host_machine.txt")
    if cache.file_exists(file_name):
      return cache.read_file(file_name)
  return get_default_hostname()


def get_client():
  global __MONGO_CLIENT
  if __MONGO_CLIENT is None:
    __MONGO_CLIENT = MongoClient(host=get_hostname())
  try:
    __MONGO_CLIENT.address
    return __MONGO_CLIENT
  except Exception:
    __MONGO_CLIENT.close()
    __MONGO_CLIENT = None
    raise RuntimeError("Looks like client is down")


def get_dataset_db(dataset):
  if not dataset:
    raise RuntimeError("Dataset is empty")
  try:
    return get_client().get_database(dataset)
  except Exception as e:
    LOGGER.warn("Dataset '%s' does not exist. Creating this mongo manually and rerun "
                "the application. Don't forget to insert dummy record" % dataset)
    raise RuntimeError(e)


def get_collection(dataset, collection_name):
  return get_dataset_db(dataset).get_collection(collection_name)



if __name__ == "__main__":
  print(get_dataset_db("codejam"))
