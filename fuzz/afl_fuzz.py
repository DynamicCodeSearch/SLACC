from __future__ import print_function, division
import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import afl
import logging
import csv
from utils.logger import get_logger
from utils import cache
from cryptography.hazmat.primitives.asymmetric.utils import (
  decode_rfc6979_signature
)

LOG_LEVEL = logging.INFO
logger = get_logger(__name__, LOG_LEVEL)
csv.field_size_limit(sys.maxsize)

