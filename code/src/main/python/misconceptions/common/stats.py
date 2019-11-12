import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


from scipy.stats.stats import pearsonr, f_oneway
import numpy as np

from utils import logger
from misconceptions.common import compare, mongo_driver, props, datatypes

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))

def check_correlation():
  store = mongo_driver.MongoStore(props.DATASET)
  diffs = store.load_differences(projection={"diff": False})
  asts = []
  ngrams = []
  levenshteins = []
  for i, diff in enumerate(diffs):
    if i % 1000 == 0:
      print(i)
    # if i == 5000:
    #   break
    ast = diff.get('d_ast', None)
    ngram = diff.get('d_n_gram', None)
    lev = diff.get('d_levenshtein', None)
    if ast is None or ngram is None or lev is None:
      continue
    asts.append(ast)
    ngrams.append(ngram)
    levenshteins.append(lev)
  print("## Pearson Correlation")
  print("AST-Ngram", pearsonr(asts, ngrams))
  print("AST-Levenshtein", pearsonr(asts, levenshteins))
  print("Ngram-Levenshtein", pearsonr(ngrams, levenshteins))


def check_anova():
  store = mongo_driver.MongoStore(props.DATASET)
  LOGGER.info("Processing for R-Py")
  diffs = store.load_differences(projection={"diff": False})
  rpy_asts = []
  rpy_ngrams = []
  rpy_levenshteins = []
  for i, diff in enumerate(diffs):
    if i % 10000 == 0:
      LOGGER.info("Processed R-Py: %d ..." % i)
    # if i == 50000:
    #   break
    ast = diff.get('d_ast', None)
    ngram = diff.get('d_n_gram', None)
    lev = diff.get('d_levenshtein', None)
    if ast is None or ngram is None or lev is None:
      continue
    rpy_asts.append(ast)
    rpy_ngrams.append(ngram)
    rpy_levenshteins.append(lev)
  LOGGER.info("Processing for Python")
  py_diffs = store.load_self_syntactic_differences(language=props.TYPE_PYTHON)
  py_asts = []
  py_ngrams = []
  py_levenshteins = []
  for i, diff in enumerate(py_diffs):
    if i % 10000 == 0:
      LOGGER.info("Processed Python: %d ..." % i)
    # if i == 50000:
    #   break
    ast = diff.get('d_ast', None)
    ngram = diff.get('d_n_gram', None)
    lev = diff.get('d_levenshtein', None)
    if ast is None or ngram is None or lev is None:
      continue
    py_asts.append(ast)
    py_ngrams.append(ngram)
    py_levenshteins.append(lev)
  LOGGER.info("Processing for R")
  r_diffs = store.load_self_syntactic_differences(language=props.TYPE_R)
  r_asts = []
  r_ngrams = []
  r_levenshteins = []
  for i, diff in enumerate(r_diffs):
    if i % 10000 == 0:
      LOGGER.info("Processed R: %d ..." % i)
    # if i == 50000:
    #   break
    ast = diff.get('d_ast', None)
    ngram = diff.get('d_n_gram', None)
    lev = diff.get('d_levenshtein', None)
    if ast is None or ngram is None or lev is None:
      continue
    r_asts.append(ast)
    r_ngrams.append(ngram)
    r_levenshteins.append(lev)
  print("\n### AST distance")
  f_measure, p_value = f_oneway(rpy_asts, py_asts, r_asts)
  print("F-Measure: %f, p-value: %f" % (f_measure, p_value))
  print("R-Py => Mean: %f, Std: %f" % (np.asscalar(np.mean(rpy_asts)), np.asscalar(np.var(rpy_asts))))
  print("Py => Mean: %f, Std: %f" % (np.asscalar(np.mean(py_asts)), np.asscalar(np.var(py_asts))))
  print("R => Mean: %f, Std: %f" % (np.asscalar(np.mean(r_asts)), np.asscalar(np.var(r_asts))))
  f_measure, p_value = f_oneway(rpy_asts, py_asts)
  print("Rpy-Py => F-Measure: %f, p-value: %f" % (f_measure, p_value))
  f_measure, p_value = f_oneway(rpy_asts, r_asts)
  print("Rpy-R => F-Measure: %f, p-value: %f" % (f_measure, p_value))
  f_measure, p_value = f_oneway(py_asts, r_asts)
  print("Py-R => F-Measure: %f, p-value: %f" % (f_measure, p_value))
  print("\n### N-Gram distance")
  f_measure, p_value = f_oneway(rpy_ngrams, py_ngrams, r_ngrams)
  print("F-Measure: %f, p-value: %f" % (f_measure, p_value))
  print("R-Py => Mean: %f, Std: %f" % (np.asscalar(np.mean(rpy_ngrams)), np.asscalar(np.var(rpy_ngrams))))
  print("Py => Mean: %f, Std: %f" % (np.asscalar(np.mean(py_ngrams)), np.asscalar(np.var(py_ngrams))))
  print("R => Mean: %f, Std: %f" % (np.asscalar(np.mean(r_ngrams)), np.asscalar(np.var(r_ngrams))))
  f_measure, p_value = f_oneway(rpy_ngrams, py_ngrams)
  print("Rpy-Py => F-Measure: %f, p-value: %f" % (f_measure, p_value))
  f_measure, p_value = f_oneway(rpy_ngrams, r_ngrams)
  print("Rpy-R => F-Measure: %f, p-value: %f" % (f_measure, p_value))
  f_measure, p_value = f_oneway(py_ngrams, r_ngrams)
  print("Py-R => F-Measure: %f, p-value: %f" % (f_measure, p_value))
  print("\n### Levenshtein distance")
  f_measure, p_value = f_oneway(rpy_levenshteins, py_levenshteins, r_levenshteins)
  print("F-Measure: %f, p-value: %f" % (f_measure, p_value))
  print("R-Py => Mean: %f, Std: %f" % (np.asscalar(np.mean(rpy_levenshteins)), np.asscalar(np.var(rpy_levenshteins))))
  print("Py => Mean: %f, Std: %f" % (np.asscalar(np.mean(py_levenshteins)), np.asscalar(np.var(py_levenshteins))))
  print("R => Mean: %f, Std: %f" % (np.asscalar(np.mean(r_levenshteins)), np.asscalar(np.var(r_levenshteins))))
  f_measure, p_value = f_oneway(rpy_levenshteins, py_levenshteins)
  print("Rpy-Py => F-Measure: %f, p-value: %f" % (f_measure, p_value))
  f_measure, p_value = f_oneway(rpy_levenshteins, r_levenshteins)
  print("Rpy-R => F-Measure: %f, p-value: %f" % (f_measure, p_value))
  f_measure, p_value = f_oneway(py_levenshteins, r_levenshteins)
  print("Py-R => F-Measure: %f, p-value: %f" % (f_measure, p_value))

def func_a15e(lst):
  lst_sorted = sorted(y)
  return lst_sorted[0]


if __name__ == "__main__":
  check_anova()
