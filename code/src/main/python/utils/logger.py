import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


import logging

DEFAULT_LEVEL = logging.DEBUG
DEFAULT_CONFIG = [
  (logging.StreamHandler(), logging.Formatter("[%(asctime)s] [%(levelname)s] [%(filename)s] %(message)s")),
]

DEFAULT_HANDLERS = []
loggers = {}

for handler, formatter in DEFAULT_CONFIG:
  handler.setFormatter(formatter)
  DEFAULT_HANDLERS.append(handler)


def configure(logger, level):
  """
  Configure Logger for a file
  :param logger: Instance fo logger
  :param level: Level of logging
  :return: Instance of logger
  """
  logger.setLevel(level)
  for d_handler in DEFAULT_HANDLERS:
    logger.addHandler(d_handler)
  return logger


def get_logger(name, level=DEFAULT_LEVEL):
  """
  Return Logger
  :param name:
  :param level:
  :return:
  """
  if name in loggers:
    return loggers[name]
  else:
    logger = configure(logging.getLogger(name), level)
    loggers[name] = logger
    return logger
