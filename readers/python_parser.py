from __future__ import print_function, division
import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import csv
import random
import ast, asttokens
import logging
from utils.logger import get_logger
from utils import cache

LOG_LEVEL = logging.INFO

logger = get_logger(__name__, LOG_LEVEL)


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
      with open("utils/cache.py") as f1:
        # ast_tokens = asttokens.ASTTokens(row['content'], parse=True)
        ast_tokens = asttokens.ASTTokens(f1.read(), parse=True)

        for node in ast.walk(ast_tokens.tree):
          if isinstance(node, ast.FunctionDef):
            ast.ge
            print(ast.get_docstring(node))
            # print(ast_tokens.get_text(node))
      # print(cnt)
      # print(row)
      exit()
  # save_file = "data/cfiles_dump/cleaned/%s.pkl" % prefix
  # cache.save(save_file, cleaned)


if __name__ == "__main__":
  clean_and_dump("data/pyfiles_dump/csv/000000000000.csv")
