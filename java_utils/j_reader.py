from __future__ import print_function, division
import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


from utils.logger import get_logger
from utils import cache
import logging
import csv

LOG_LEVEL = logging.INFO
logger = get_logger(__name__, LOG_LEVEL)
csv.field_size_limit(sys.maxsize)
BASE_GITHUB = "https://github.com"


def handled_csv_reader(csv_reader):
  """
  A modified version of CSV reader with handles CSV formatting error
  :param csv_reader: CSV reader
  :return:
  """
  while True:
    try:
      yield next(csv_reader)
    except csv.Error:
      pass
    continue
  return


def get_header_and_row_count(file_name):
  """
  Access header and get number of rows
  in the csv file
  :param file_name: Name of csv file
  :return: (Header, Number of rows in csv file)
  """
  with open(file_name, "rb") as csv_file:
    header = None
    header_reader = handled_csv_reader(csv.reader(csv_file))
    cnt = 0
    for row in header_reader:
      if header is None:
        header = row
      else:
        cnt += 1
    return header, cnt


def extract_java_repos(source_file, save_file):
  """
  Extract all java repos from the source file
  :param source_file: CSV of list of all projects from github.
  :param save_file: .pkl file to save set of java project URLs
  :return:
  """
  header, row_count = get_header_and_row_count(source_file)
  java_repos = set()
  with open(source_file) as csv_file:
    header_reader = handled_csv_reader(csv.reader(csv_file))
    for _ in header_reader: break
    reader = handled_csv_reader(csv.DictReader(csv_file, header))
    cnt = 0
    for row in reader:
      cnt += 1
      if row['language'] == "Java":
        java_repos.add("%s/%s" % (BASE_GITHUB, row['repository']))
      if cnt % 100 == 0:
        logger.info("Processed %d/%d lines. # Java Repos = %d" % (cnt, row_count, len(java_repos)))
  cache.save(save_file, java_repos)
  logger.info("Finished processing. # Java Repos = %d/%d" % (len(java_repos), row_count))


def _extract_java_repos():
  source_file = "data/javafiles_dump/repo_reaper.csv"
  save_file = "data/javafiles_dump/repo_urls.pkl"
  extract_java_repos(source_file, save_file)


if __name__ == "__main__":
  _extract_java_repos()
