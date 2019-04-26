import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import random
import pandas as pd
import numpy as np
import inflect
from collections import OrderedDict

from utils import cache, lib, logger
from misconceptions.common import datatypes, props, mongo_driver

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))
INFLECTOR = inflect.engine()
SAMPLE_INPUT_FILE = os.path.join(props.RESOURCES_HOME, "titanic.csv")
GENERATED_INPUT_PKL = os.path.join(props.RESOURCES_HOME, "generated_inputs.pkl")


class DataFrameGenerator(lib.O2):
  def __init__(self, **kwargs):
    self.max_rand_rows = 100
    self.max_rand_cols = 20
    lib.O2.__init__(self, **kwargs)

  def generate(self, df_template):
    data = OrderedDict()
    n_rows = np.random.randint(1, self.max_rand_rows + 1)
    series_generator = SeriesGenerator(n_values=n_rows)
    for col_name, column in df_template.columns.items():
      data[col_name] = series_generator.generate(column)
    return pd.DataFrame(data=data)


class SeriesGenerator(lib.O2):
  def __init__(self, n_values, nan_prob=0.1):
    self.n_values = n_values
    self.nan_prob = nan_prob
    lib.O2.__init__(self)

  def generate(self, template):
    if template.levels:
      arr = self.generate_levels(template)
    elif template.type == int:
      arr = self.generate_int(template)
    elif template.type == float:
      arr = self.generate_float(template)
    elif template.type == bool:
      arr = self.generate_bool(template)
    elif template.type == str:
      arr = self.generate_str(template)
    else:
      raise RuntimeError("WTF is the type: %s" % template.type)
    if template.has_NAN:
      for i in xrange(len(arr)):
        chance = random.random()
        if chance < self.nan_prob:
          if template.type in {int, float}:
            arr[i] = np.NAN
          else:
            arr[i] = ''
    return np.asarray(arr)

  def generate_int(self, template):
    return np.random.randint(template.min, template.max + 1, self.n_values, int)

  def generate_float(self, template):
    return np.random.uniform(template.min, template.max, size=(self.n_values,))

  def generate_bool(self, template):
    return np.random.randint(0, 2, self.n_values, bool)

  def generate_str(self, template):
    if template.values is not None:
      return [random.choice(template.values) for _ in xrange(self.n_values)]
    else:
      return [INFLECTOR.number_to_words(i) for i in np.random.randint(0, self.n_values + 1, self.n_values, int)]

  def generate_levels(self, template):
    return [random.choice(template.levels) for _ in xrange(self.n_values)]


def get_df_metadata(sample_input_file):
  name = cache.get_file_name(sample_input_file)
  data = pd.read_csv(sample_input_file)
  cols = data.columns
  df = datatypes.DataFrame()
  df.name = name
  df_cols = OrderedDict()
  for col in cols:
    series = datatypes.Series()
    series.name = col
    series.type = to_native_type(data.dtypes[col])
    values = data[col]
    series.has_NAN = values.isna().sum() > 0
    if series.has_NAN:
      values = values[~pd.isnull(values)].tolist()
    uniques = set(values)
    if len(uniques) < 0.1 * len(values):
      series.levels = sorted(list(uniques))
    else:
      if series.type in {int, float}:
        series.min = min(values)
        series.max = max(values)
      else:
        series.values = values
    df_cols[col] = series
  df.columns = df_cols
  return df


def to_native_type(np_type):
  type_name = np_type.name
  if type_name.startswith("int"):
    return int
  elif type_name.startswith("float"):
    return float
  elif type_name.startswith("object"):
    return str
  else:
    raise Exception("WTF is the type %s" % type_name)


def generate_args(force=False, n_args=256, max_rand_rows=100):
  store = mongo_driver.MongoStore(props.DATASET)
  df_metadata = get_df_metadata(SAMPLE_INPUT_FILE)
  column_names = df_metadata.columns.keys()
  if not force:
    existing = store.load_inputs(column_names)
    if existing:
      LOGGER.info("Loading existing args ... ")
      return existing
  LOGGER.info("Generating fresh set of args and saving ... ")
  generator = DataFrameGenerator(max_rand_rows=max_rand_rows)
  args = []
  for _ in xrange(n_args):
    arg_set = [generator.generate(df_metadata)]
    args.append(arg_set)
  store.delete_inputs()
  store.save_inputs(args)
  return args


def _test_meta():
  print(get_df_metadata(SAMPLE_INPUT_FILE).columns.keys())


def _test_generate_args():
  # print(generate_args(force=True, n_args=1, max_rand_rows=6))
  args = generate_args(force=True)
  print(pd.DataFrame(args[0][0].to_dict(orient='list')))


if __name__ == "__main__":
  _test_meta()
  # generate_args()
  # _test_generate_args()
