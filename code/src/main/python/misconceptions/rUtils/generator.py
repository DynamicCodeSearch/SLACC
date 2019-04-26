import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


import numpy as np
import pandas as pd
import random
import inflect


from utils import cache, logger, lib
from misconceptions.common import datatypes

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))
STORE_PATH = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/src/main/python/expt/store.pkl"
INFLECTOR = inflect.engine()


class VectorGenerator(lib.O):
  def __init__(self, **kwargs):
    self.n_values = 100
    self.types = [int, bool, float, str]
    self.int_range = [-100, 100]
    self.float_range = [-100.0, 100.0]
    self.max_levels = 10
    lib.O.__init__(self, **kwargs)

  def generate(self, vector_template):
    if vector_template is None or vector_template.type is None:
      fn = random.choice([self.generate_str, self.generate_bool, self.generate_int, self.generate_float])
      return fn(vector_template)
    elif vector_template.type == int:
      return self.generate_int(vector_template)
    elif vector_template.type == float:
      return self.generate_float(vector_template)
    elif vector_template.type == bool:
      return self.generate_bool(vector_template)
    elif vector_template.type == str:
      return self.generate_str(vector_template)

  def generate_int(self, vector_template):
    return np.random.randint(self.int_range[0], self.int_range[1]+1, self.n_values, int)

  def generate_float(self, vector_template):
    return np.random.uniform(low=self.float_range[0], high=self.float_range[1], size=(self.n_values,))

  def generate_bool(self, vector_template):
    return np.random.randint(0, 2, self.n_values, bool)

  def generate_str(self, vector_template):
    if vector_template is None or vector_template.levels is None:
      levels = [INFLECTOR.number_to_words(i) for i in xrange(self.max_levels)]
    else:
      levels = vector_template.levels
    return [random.choice(levels) for _ in xrange(self.n_values)]


class DataFrameGenerator(lib.O):
  def __init__(self, **kwargs):
    self.max_rand_rows = 100
    self.max_rand_cols = 20
    lib.O.__init__(self, **kwargs)

  def generate(self, df_template):
    if df_template is None:
      return generate_random_dataframe()
    else:
      n_cols = len(df_template.columns) + np.random.randint(0, self.max_rand_cols, dtype=int)
      n_rows = np.random.randint(1, self.max_rand_rows + 1)
      data = {}
      vectorGenerator = VectorGenerator(n_values=n_rows)
      for col_name, column in df_template.columns.items():
        data[col_name] = vectorGenerator.generate(column)
      for i in range(len(data), n_cols):
        col_name = "gen_col_%d" % i
        data[col_name] = vectorGenerator.generate(None)
      return pd.DataFrame(data=data)


def generate_dataframe(n_rows, n_cols, make_col_names):
  data = np.random.randint(-100, 100, (n_rows, n_cols))
  col_names = None
  if make_col_names:
    col_names = ["SLAAC_col%d" % (i + 1) for i in xrange(n_cols)]
  df = pd.DataFrame(data, columns=col_names)
  return df


def generate_named_dataframe(n_rows, n_cols, columns):
  col_names = list(columns.keys())
  data = np.random.randint(-100, 100, (n_rows, n_cols))
  pd_col_names = col_names + ["SLAAC_col%d" % (i + 1) for i in xrange(n_cols - len(col_names))]
  df = pd.DataFrame(data, columns=pd_col_names)
  col_headers = df.columns.values
  random.shuffle(col_headers)
  df = df[col_headers]
  return df


def generate_args_from_sample(sample_variables, n_args):
  generators = []
  for name, sample_variable in sample_variables.items():
    if type(sample_variable) == datatypes.DataFrame:
      generators.append(DataFrameGenerator())
    else:
      raise RuntimeError("For now we do not support '%s'" % type(datatypes.DataFrame))
  generated_args = []
  for _ in xrange(n_args):
    args = []
    for i, (name, sample_variable) in enumerate(sample_variables.items()):
      args.append(generators[i].generate(sample_variable))
    generated_args.append(args)
  return generated_args

# def generate_R_dataframe(n_rows, n_cols, make_col_names):
#   df = generate_dataframe(n_rows, n_cols, make_col_names)
#   return pandas2ri.py2ri(df)


def generate_random_dataframe(columns=None):
  delta = len(columns) if columns else 0
  n_rows = np.random.randint(1, 101)
  n_cols = np.random.randint(1 + delta, 20 + delta)
  if delta:
    return generate_named_dataframe(n_rows, n_cols, columns)
  else:
    make_col_names = np.random.choice([True, False])
    return generate_dataframe(n_rows, n_cols, make_col_names)


def make_key(data_types):
  comps = []
  sep = "$|$"
  for name, props in data_types.items():
    if datatypes.is_dataframe_type(props["type"]):
      if "col_names" in props and props["col_names"]:
        col_names = []
        for col_name, series in props["col_names"].items():
          col_names.append(col_name)
        comps.append("DataFrame[%s]" % "@|@".join(col_names))
      else:
        comps.append("DataFrame")
  return sep.join(comps)


def generate_args(data_types, n_args):
  args = []
  for _ in xrange(n_args):
    arg = []
    for arg_name, props in data_types.items():
      if datatypes.is_dataframe_type(props["type"]):
        if "col_names" in props:
          arg.append(generate_random_dataframe(props["col_names"]))
        else:
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
  # print(convert_py_object_to_r(generate_dataframe(4, 3, True)))
  # print(generate_named_dataframe(3,5,["Hello", "World"]))
  print(VectorGenerator().generate_bool())