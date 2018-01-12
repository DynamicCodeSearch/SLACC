from __future__ import print_function, division
import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


import csv
import random
import re
from utils import cache
import logging
from utils.logger import get_logger
from sklearn.feature_extraction.text import CountVectorizer

LOG_LEVEL = logging.INFO

logger = get_logger(__name__, LOG_LEVEL)

csv.field_size_limit(sys.maxsize)


def comment_remover(text):
  def replacer(match):
    s = match.group(0)
    if s.startswith('/'):
      return ""
    else:
      return s

  pattern = re.compile(
      r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
      re.DOTALL | re.MULTILINE
  )
  return re.sub(pattern, replacer, text)


def clean_and_dump(file_name, select_prob=1.0):
  prefix = file_name.rsplit("/", 1)[-1].split(".")[0]
  logger.info("Running for %s" % prefix)
  with open(file_name) as csv_file:
    header = None
    header_reader = csv.reader(csv_file)
    for row in header_reader:
      header = row
      break
    reader = csv.DictReader(csv_file, header)
    cnt = 0
    cleaned = []
    for row in reader:
      if random.random() > select_prob:
        continue
      cnt += 1
      # print(cnt)
      cleaned.append(comment_remover(row['content']))
  save_file = "data/cfiles_dump/cleaned/%s.pkl" % prefix
  cache.save(save_file, cleaned)


def dump_clean_folder(folder, select_prob=1.0):
  files = sorted(os.listdir(folder))
  for i, f_name in enumerate(files):
    if f_name == ".DS_Store":
      continue
    clean_and_dump("%s/%s" % (folder, f_name), select_prob)
    logger.info("Completed %d of %d" % (i + 1, len(files)))


def tokenize(file_name, token_pattern=r"(?u)\b[a-zA-Z_]{1,100}\b"):
  prefix = file_name.rsplit("/", 1)[-1].split(".")[0]
  logger.info("Running Tokenizer for %s" % prefix)
  analyzer = CountVectorizer(token_pattern=token_pattern).build_analyzer()
  snippets = cache.load(file_name)
  tokenized = []
  for snippet in snippets:
    tokenized.append(analyzer(snippet))
  save_file = "data/cfiles_dump/tokenized/%s.pkl" % prefix
  cache.save(save_file, tokenized)


def tokenize_folder(folder):
  files = sorted(os.listdir(folder))
  for i, f_name in enumerate(files):
    if f_name == ".DS_Store":
      continue
    tokenize("%s/%s" % (folder, f_name))
    logger.info("Completed %d of %d" % (i + 1, len(files)))


if __name__ == "__main__":
  # dump_clean_folder("data/cfiles_dump/csv", 0.2)
  tokenize_folder("data/cfiles_dump/cleaned")
