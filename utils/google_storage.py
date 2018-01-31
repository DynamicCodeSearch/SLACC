from __future__ import print_function, division
import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from utils import lib
from google.cloud import storage
from utils.cache import mkdir, file_exists
from joblib import Parallel, delayed


BUCKET_NAME = "enableviz-1380.appspot.com"
STORAGE_CLIENT = storage.Client()
BUCKET = STORAGE_CLIENT.get_bucket(BUCKET_NAME)


def implicit():
  """
  Check if client is validly configured
  """
  storage_client = storage.Client()
  # Make an authenticated API request
  buckets = list(storage_client.list_buckets())
  print(buckets)


def get_blob(name):
  return BUCKET.blob(name)


def download_blob(name, download_path):
  """
  Download a blob from Google Cloud Storage
  :param name: Name of Blob
  :param download_path: Path to be saved
  """
  blob = get_blob(name)
  name = blob.name.rsplit("/", 1)[-1]
  if download_path[-1] == "/":
    destination_file = "%s%s" % (download_path, name)
  else:
    destination_file = "%s/%s" % (download_path, name)
  if file_exists(destination_file):
    print("%s already exists" % destination_file)
    return name
  else:
    blob.download_to_filename(destination_file)
    print('Blob {} downloaded to {}.'.format(name, destination_file))
  return name


def download_blobs(prefix_path, download_path, n_jobs, max_results=None, do_parallel=False):
  """
  :param prefix_path:
  :param download_path:
  :param n_jobs:
  :param max_results:
  :param do_parallel
  :return:
  """
  mkdir(download_path)
  blobs = []
  for stat in BUCKET.list_blobs(prefix=prefix_path):
    if stat.size == 0:
      continue
    blobs.append(stat.name)
    if max_results is not None and len(blobs) >= max_results:
      break
  print("# Files =", len(blobs))
  if do_parallel:
    Parallel(n_jobs=n_jobs)(delayed(download_blob)(name, download_path) for name in blobs)
  else:
    for name in blobs:
      download_blob(name, download_path)


def _download_blobs(source, destination, max_results=None):

  n_jobs = 1
  # source, max_results = "pyfiles/csv/", 2
  # source, max_results = "pyfiles/csv_all/", None
  do_parallel = False
  args = sys.argv
  if len(args) >= 2 and lib.is_int(args[1]):
    n_jobs = int(args[1])
  print("Running as %d jobs" % n_jobs)
  download_blobs(source, destination, n_jobs, max_results, do_parallel=do_parallel)

if __name__ == "__main__":
  # implicit()
  _download_blobs("cfiles/csv", "data/cfiles_dump/csv")

