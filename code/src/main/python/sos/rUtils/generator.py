import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


import numpy as np
import pandas as pd
from rpy2.robjects import pandas2ri

from utils import cache, logger

pandas2ri.activate()

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))
STORE_PATH = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/src/main/python/expt/store.pkl"


def generate_dataframe(n_rows, n_cols, make_col_names):
  data = np.random.randint(-100, 100, (n_rows, n_cols))
  col_names = None
  if make_col_names:
    col_names = ["col%d" % (i + 1) for i in xrange(n_cols)]
  df = pd.DataFrame(data, columns=col_names)
  return df


def generate_R_dataframe(n_rows, n_cols, make_col_names):
  df = generate_dataframe(n_rows, n_cols, make_col_names)
  return pandas2ri.py2ri(df)


def generate_random_dataframe():
  n_rows = np.random.randint(1, 101)
  n_cols = np.random.randint(1, 20)
  make_col_names = np.random.choice([True, False])
  return generate_dataframe(n_rows, n_cols, make_col_names)


def is_dataframe_type(data_type):
  name = data_type.__name__
  return name.endswith("DataFrame")


def make_key(data_types):
  comps = []
  sep = "$|$"
  for dt in data_types:
    if is_dataframe_type(dt):
      comps.append("DataFrame")
  return sep.join(comps)


def convert_py_object_to_r(py_obj):
  if type(py_obj) == pd.core.frame.DataFrame:
    return pandas2ri.py2ri(py_obj)
  raise RuntimeError("Currently does not support type: %s" % type(py_obj))


def convert_r_object_to_py(r_obj):
  return pandas2ri.ri2py(r_obj)


def generate_args(data_types, n_args):
  args = []
  for _ in xrange(n_args):
    arg = []
    for data_type in data_types:
      if is_dataframe_type(data_type):
        arg.append(generate_random_dataframe())
      else:
        raise RuntimeError("Supports only dataframes")
    args.append(arg)
  return args


def store_args(key, args):
  data_store = cache.load_pickle(STORE_PATH)
  if not data_store:
    data_store = {}
  data_store[key] = args
  cache.save_pickle(STORE_PATH, data_store)


def load_args(data_types):
  key = make_key(data_types)
  data_store = cache.load_pickle(STORE_PATH)
  if data_store and key in data_store:
    arg_sets = data_store[key]
  else:
    LOGGER.info("Generating random arguments for the key '%s'" % key)
    arg_sets = generate_args(data_types, 100)
    store_args(key, arg_sets)
  return arg_sets


if __name__ == "__main__":
  # print(len(load_args([type(generate_R_dataframe(4, 3, True))])))
  # print(type(generate_R_dataframe(4, 3, True)).__name__)
  print(convert_py_object_to_r(generate_dataframe(4, 3, True)))
