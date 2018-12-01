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
    LOGGER.info("Running for all codejam projects ... ")
    execute.extract_metadata_for_folder(properties.CODE_JAM)
  else:
    LOGGER.info("Running for the codejam project: %s ... " % args[1])
    execute.extract_metadata_for_folder(properties.CODE_JAM, args[1])
