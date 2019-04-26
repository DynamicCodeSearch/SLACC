import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from utils import cache, logger, stat
from sos.function import Function, Outputs
from sos.clusterer import RepresentativeClusterer
import pandas as pd
import numpy as np
import re
from misconceptions.rUtils import generator, dataframer
from misconceptions.common.differences import DataFrameDiffMeta


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))
PD_FUNCTIONS_PATH = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/src/main/python/expt/pd_functions.pkl"
R_FUNCTIONS_PATH = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/src/main/python/expt/r_functions.pkl"
BASE_CLUSTER_FOLDER = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/src/main/python/expt"


LST_TYPES = {tuple, list, np.ndarray}


def is_equal(val1, val2):
  t_1, t_2 = type(val1), type(val2)
  if t_1 == t_2 == pd.DataFrame:
    ret_val = val1.values == val2.values
  elif t_1 == pd.DataFrame:
    return val1.empty and not val2
  elif t_2 == pd.DataFrame:
    return val2.empty and not val1
  elif t_1 in LST_TYPES and t_2 in LST_TYPES:
    ret_val = val1 == val2
  elif type(val1) != type(val2):
    ret_val = False
  else:
    ret_val = val1 == val2
  if type(ret_val) == np.ndarray:
    return ret_val.all()
  return ret_val


def is_useful_function(funct):
  if funct.useful is not None:
    return funct.useful
  only_none = True
  return_not_nones_indices = []
  last_return_value = None
  returns_same_value = True
  for i, retrn in enumerate(funct.outputs.returns):
    if retrn is not None:
      only_none = False
      # print("Last", last_return_value)
      # print("Current", retrn)
      # print("*********\n")
      if last_return_value is None:
        last_return_value = retrn
      elif returns_same_value and not is_equal(last_return_value, retrn):
        returns_same_value = False
      return_not_nones_indices.append(i)
  # If outputs contain only None
  if only_none:
    funct.useful = False
    return funct.useful
  # If it returns same value
  if returns_same_value:
    funct.useful = False
    return funct.useful
  # If contains non return indices
  if len(return_not_nones_indices) == 0:
    funct.useful = False
    return funct.useful
  funct.useful = True
  return funct.useful


def is_same_error(e1, e2):
  return (e1 is None and e2 is None) or (e1 is not None and e2 is not None)


def execution_similarity(func1, func2):
  if func1.input_key != func2.input_key:
    return 0.0
  sames = 0.0
  alls = 0.0
  assert len(func1.outputs.returns) == len(func2.outputs.returns)
  for i in range(len(func1.outputs.returns)):
    alls += 1
    o1 = func1.outputs.returns[i]
    o2 = func2.outputs.returns[i]
    e1 = func1.outputs.errors[i]
    e2 = func2.outputs.errors[i]
    # print(o1)
    # print(o2)
    # print("*************")
    if is_equal(o1, o2) and is_same_error(e1, e2):
      sames += 1
  return sames / alls


def execution_distance(func1, func2):
  return 1.0 - execution_similarity(func1, func2)


def get_body(func_dict):
  return re.sub('<bytecode: 0x[0-9a-z]+>', '', func_dict['body']).strip() + "\n"


def load_functions(functions_path, source):
  functions_dict = cache.load_pickle(functions_path)
  functions = []
  for func_name, func_dict in functions_dict.items():
    outputs = Outputs(func_dict["outputs"])
    funct = Function(name=func_name, input_key=func_dict["inputKey"],
                     outputs=outputs, body=get_body(func_dict), source=source)
    functions.append(funct)
  valid_functions = {funct.name: funct for funct in functions if is_useful_function(funct)}
  LOGGER.info("Valid Functions : %d / %d" % (len(valid_functions), len(functions)))
  return valid_functions


def cluster(clustering_error):
  functions = load_functions(PD_FUNCTIONS_PATH, "pandas")
  functions.update(load_functions(R_FUNCTIONS_PATH, "R"))
  file_name = "clusters"
  folder = os.path.join(BASE_CLUSTER_FOLDER, "%0.02f" % clustering_error)
  cache.mkdir(folder)
  clusters_txt_file = os.path.join(folder, "%s.txt" % file_name)
  clusters_pkl_file = os.path.join(folder, "%s.pkl" % file_name)
  clusters_report_file = os.path.join(folder, "%s.md" % file_name)
  clusterer = RepresentativeClusterer(functions.values(), distance_function=execution_distance)
  clusters = clusterer.cluster(clusters_txt_file, skip_singles=True, clustering_error=clustering_error)
  cache.save_pickle(clusters_pkl_file, clusters)
  n_clusters = len(clusters)
  sizes = [len(cluster_funcs) for label, cluster_funcs in clusters.items() if label != -1]
  meta_data = "## Cluster sizes\n"
  meta_data += "* Number of clusters: %d\n" % n_clusters
  meta_data += "* Number of functions clustered: %d\n" % sum(sizes)
  meta_data += "* Number of functions not clustered: %d\n\n" % (len(functions) - sum(sizes))
  meta_data += "## REPORT\n"
  meta_data += stat.Stat(sizes).report()
  cache.write_file(clusters_report_file, meta_data)


def similar_matching(py_func_name, r_func_name):
  # args = generator.load_args([pd.DataFrame])
  functions = load_functions(PD_FUNCTIONS_PATH, "pandas")
  functions.update(load_functions(R_FUNCTIONS_PATH, "R"))
  pd_function = functions[py_func_name]
  r_function = functions[r_func_name]
  metas = []
  for i in xrange(len(pd_function.outputs.returns)):
    pd_i = pd_function.outputs.returns[i]
    r_i = r_function.outputs.returns[i]
    df_meta = dataframer.difference(pd_i, r_i)
    # if df_meta.sim_score < 0.1:
    #   print(args[i])
    #   print(df_meta)
    #   print(pd_i)
    #   print(r_i)
    #   print(dataframer.difference(pd_i, r_i))
    #   print(df_meta)
    #   exit()
    metas.append(df_meta)
  return DataFrameDiffMeta.aggregate(metas)


def _similar():
  py_func_name = "func_py_0_1_index"
  r_func_name = "gen_func_r_0_1_index"
  print(similar_matching(py_func_name, r_func_name))


def _test():
  args = generator.load_args([pd.DataFrame])
  functions = load_functions(PD_FUNCTIONS_PATH, "pandas")
  functions.update(load_functions(R_FUNCTIONS_PATH, "R"))
  pd_f_name = "func_py_select2"
  r_f_name = "gen_func_r_select2"
  pd_function = functions[pd_f_name]
  r_function = functions[r_f_name]
  print(execution_distance(pd_function, r_function))
  for i in xrange(len(pd_function.outputs.returns)):
    pd_i = pd_function.outputs.returns[i]
    r_i = r_function.outputs.returns[i]
    pd_e_i = pd_function.outputs.errors[i]
    r_e_i = r_function.outputs.errors[i]
    # print(args[i])
    # print(pd_i)
    # print(r_i)
    # print()

    # if is_equal(pd_i, r_i) and r_i is not None and not r_i.empty:
    if not is_equal(pd_i, r_i):
      # print(pd_i, r_i)
      print(args[i])
      print(pd_i)
      print(r_i)
      exit(0)
    # if pd_i is not None:
    #   print(pd_i)
    #   print(r_i)
    #   print(pd_i.as_matrix() == r_i.as_matrix())
    #   #
    #   print(assert_frame_equal(pd_i, r_i, check_dtype=False))
    #   exit(0)


def _cluster():
  args = sys.argv
  error = 0.01 if len(args) < 2 else float(args[1])
  cluster(error)


if __name__ == "__main__":
  # _cluster()
  # _test()
  _similar()
