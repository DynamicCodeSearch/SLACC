import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from analysis import execute
from utils import logger
import properties


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


if __name__ == "__main__":
  args = sys.argv
  if len(args) < 2:
    print("Use python codejam/function_metadata.py <dataset> <?problem_id>")
    exit(0)
  elif len(args) > 2:
    LOGGER.info("Running for dataset: %s, project: %s ... " % (args[1], args[2]))
    execute.extract_metadata_for_folder(args[1], args[2])
  else:
    LOGGER.info("Running for dataset: %s ... " % args[1])
    execute.extract_metadata_for_folder(args[1])
