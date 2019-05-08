import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import numpy as np
import pandas as pd
import time
import multiprocessing
from Queue import Queue

from utils import lib, cache, logger
from sos.function import Outputs
from misconceptions.common import mongo_driver, props
from misconceptions.common.differences import DataFrameDiffMeta, ArrayDiffMeta, MatrixDiffMeta, DiffMeta

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))
LST_TYPES = {tuple, list, np.ndarray}


class Statement(lib.O):
  def __init__(self, **kwargs):
    self.mongo_id = None
    self.snippet = None
    self.normalized = None
    self.variables = None
    self.language = None
    self.outputs = None
    lib.O.__init__(self, **kwargs)

  def is_all_none(self):
    for res, rets in self.outputs.items():
      if not is_all_none(rets.returns):
        return False
    return True

  def is_all_same(self):
    for res, rets in self.outputs.items():
      if not rets.is_all_same:
        return False
    return True


def get_executed_stmts_pkl(language):
  return os.path.join(props.RESOURCES_HOME, "executed_%s.pkl" % language)


def fetch_statements(language, force=False, do_save=False, limit=None, as_list=False):
  pkl_file = get_executed_stmts_pkl(language)
  if not force and cache.file_exists(pkl_file):
    LOGGER.info("Retrieving existing '%s' statements!" % language)
    if as_list:
      return cache.load_pickle(pkl_file).values()
    return cache.load_pickle(pkl_file)
  LOGGER.info("Reprocessing '%s' statements!" % language)
  store = mongo_driver.MongoStore(props.DATASET)
  stmts = {}
  mongo_stmts = store.load_stmts(language=language, is_valid=True, has_output=True, limit=limit).items()
  n_stmts = len(mongo_stmts)
  for i, (key, mongo_stmt) in enumerate(mongo_stmts):
    LOGGER.info("Processing %d / %d .... " % (i + 1, n_stmts))
    stmt = Statement(mongo_id=mongo_stmt["_id"], snippet=mongo_stmt["snippet"],
                     variables=mongo_stmt["variables"], language=language,
                     outputs=format_outputs(mongo_stmt["outputs"]))
    stmts[stmt.mongo_id] = stmt
  if do_save:
    LOGGER.info("Saving statements .... ")
    cache.save_pickle(pkl_file, stmts)
  if as_list:
    return stmts.values()
  return stmts


def format_outputs(outputs):
  formatted_outputs = {}
  for key, output in outputs.items():
    formatted = Outputs()
    formatted.is_all_same = True
    prev_vals = []
    for o in output:
      ret_formatted = format_return(o["return"]) if "return" in o else None
      formatted.returns.append(ret_formatted)
      formatted.errors.append(o["errorMessage"] if "errorMessage" in o else None)
      formatted.durations.append(o["duration"] if "duration" in o else None)
      if len(prev_vals) == 0:
        prev_vals.append(ret_formatted)
      elif formatted.is_all_same and not is_equal(ret_formatted, prev_vals[0]):
        formatted.is_all_same = False
    formatted_outputs[key] = formatted
  return formatted_outputs


def format_return(ret_val):
  if isinstance(ret_val, dict):
    try:
      return pd.DataFrame(ret_val)
    except Exception:
      return ret_val
  elif type(ret_val) in LST_TYPES:
    return np.array(ret_val)
  return ret_val


def is_equal(val1, val2):
  t_1, t_2 = type(val1), type(val2)
  if t_1 == t_2 == pd.DataFrame:
    ret_val = val1.values == val2.values
  elif t_1 == pd.DataFrame:
    return val1.empty and not val2
  elif t_2 == pd.DataFrame:
    return val2.empty and not val1
  elif t_1 in LST_TYPES and t_2 in LST_TYPES:
    f_val1 = np.array(val1)
    f_val2 = np.array(val2)
    if f_val1.shape != f_val2.shape:
      return False
    ret_val = f_val1 == f_val2
  elif type(val1) != type(val2):
    ret_val = False
  else:
    ret_val = val1 == val2
  if type(ret_val) == np.ndarray:
    return ret_val.all()
  return ret_val


def is_same_error(e1, e2):
  return (e1 is None and e2 is None) or (e1 is not None and e2 is not None)


def output_similarity(res1, res2):
  sames = 0.0
  alls = 0.0
  assert len(res1.returns) == len(res2.returns)
  for i in range(len(res1.returns)):
    alls += 1
    o1 = res1.returns[i]
    o2 = res2.returns[i]
    e1 = res1.errors[i]
    e2 = res2.errors[i]
    if is_equal(o1, o2) and is_same_error(e1, e2):
      sames += 1
  return sames / alls


def similarity(stmt1, stmt2):
  assert stmt1.language != stmt2.language
  best_score = None
  best_keys = None
  for key1, res1 in stmt1.outputs.items():
    for key2, res2 in stmt2.outputs.items():
      score = output_similarity(res1, res2)
      if not best_score or score > best_score:
        best_score = score
        best_keys = (key1, key2)
  return best_score, best_keys


def compare_values(val1, val2):
  t_1, t_2 = type(val1), type(val2)
  if t_1 == t_2:
    if t_1 == pd.DataFrame:
      return DataFrameDiffMeta.difference(val1, val2)
    elif t_1 == np.ndarray:
      if val1.ndim == val2.ndim == 1:
        return ArrayDiffMeta.difference(val1, val2)
      elif val1.ndim == val2.ndim == 2:
        return MatrixDiffMeta.difference(val1, val2)
      elif val1.ndim == 1 and val2.ndim == 2:
        return MatrixDiffMeta.difference(np.array([val1]), val2)
      elif val1.ndim == 2 and val2.ndim == 1:
        return MatrixDiffMeta.difference(val1, np.array([val2]))
      elif val1.ndim == val2.ndim:
        return DiffMeta(sim_score=0.0, types=(t_1.__name__, t_2.__name__),
                        message="Array size = %d not supported" % val1.ndim)
      else:
        return DiffMeta(sim_score=0.0, types=(t_1.__name__, t_2.__name__),
                        message="Array sizes of %d and %d not supported" % (val1.ndim, val2.ndim))
    else:
      score = 1.0 if val1 == val2 else 0.0
      return DiffMeta(sim_score=score, types=(t_1.__name__, t_2.__name__))
  else:
    return DiffMeta(sim_score=0.0, types=(t_1.__name__, t_2.__name__), message="Mismatched types")


def is_empty(val):
  t = type(val)
  if t == pd.DataFrame:
    return val.empty
  elif t == np.ndarray:
    return val.size == 0
  elif val or val == 0 or val == "" or val is False:
    return False
  return True


def is_all_none(lst):
  for x in lst:
    if not is_empty(x):
      return False
  return True


def difference(r_stmt, py_stmt, store=None, do_log=False):
  assert r_stmt.language != py_stmt.language
  if store is None:
    store = mongo_driver.MongoStore(props.DATASET)
  for r_return, res1 in r_stmt.outputs.items():
    if res1.is_all_same or is_all_none(res1.returns):
      continue
    for py_return, res2 in py_stmt.outputs.items():
      if res2.is_all_same or is_all_none(res2.returns):
        continue
      # diffs = compare_returns(res1.returns, res2.returns)
      diffs = pooled_compare_returns(res1.returns, res2.returns)
      if do_log:
        LOGGER.info("Saving R: %s, PY: %s ... " % (r_stmt.mongo_id, py_stmt.mongo_id))
      store.save_difference(r_id=r_stmt.mongo_id, py_id=py_stmt.mongo_id,
                            r_return=mongo_driver.mongo_de_escape(r_return),
                            py_return=mongo_driver.mongo_de_escape(py_return),
                            diff=diffs, do_log=do_log)


def compare_returns(rets1, rets2):
  diffs = []
  for val1, val2 in zip(rets1, rets2):
    diffs.append(compare_values(val1, val2))
  return diffs


def threaded_compare_values(q, result):
  while not q.empty():
    work = q.get()
    try:
      diff = compare_values(work[1], work[2])
      result[work[0]] = diff
    except Exception as e:
      LOGGER.error("Exception while comparing diff instance. Error '%s'" % e.message)
      result[work[0]] = None
    q.task_done()
  return True


def threaded_compare_returns(rets1, rets2):
  assert len(rets1) == len(rets2)
  q = Queue(maxsize=0)
  n_processes = multiprocessing.cpu_count()
  results = [{} for _ in xrange(len(rets1))]
  for i in xrange(len(rets1)):
    q.put((i, rets1[i], rets2[i]))
  processes = []
  for _ in xrange(n_processes):
    t = multiprocessing.Process(target=compare_values, args=(q, results,))
    processes.append(t)
    t.start()
  for p in processes:
    p.join()
  return results


def pooled_compare_values(index, val_1, val_2):
  return index, compare_values(val_1, val_2)


def pooled_compare_returns(rets1, rets2):
  assert len(rets1) == len(rets2)
  results = [{} for _ in xrange(len(rets1))]
  n_processes = min(multiprocessing.cpu_count(), len(rets1))
  # n_processes = 3
  pool = multiprocessing.Pool(processes=n_processes)
  pooled = [pool.apply_async(pooled_compare_values, args=(i, rets1[i], rets2[i])) for i in xrange(len(rets1))]
  for p in pooled:
    p = p.get()
    results[p[0]] = p[1]
  pool.close()
  pool.join()
  return results


def test_similarity(limit=None):
  r_stmts = fetch_statements(props.TYPE_R, force=True, limit=limit)
  py_stmts = fetch_statements(props.TYPE_PYTHON, force=True, limit=limit)
  r_scores = {}
  for r_id, r_stmt in r_stmts.items():
    scores = []
    for py_id, py_stmt in py_stmts.items():
      score, keys = similarity(r_stmt, py_stmt)
      scores.append([score, py_id, keys])
    scores = sorted(scores, key=lambda x: x[0], reverse=True)
    r_scores[r_id] = scores
  for r_id in r_scores.keys():
    print("### %s" % r_id)
    for r_score in r_scores[r_id]:
      print("\t %0.2f: %s => %s, %s" % (r_score[0], r_score[1], r_score[2][0], r_score[2][1]))
    print("")
  return r_scores


def runner(skip_threshold=3500, start=0, end=None, use_normalized=False):
  LOGGER.info("Computing differences for R stmts b/w %d and %d on %d processes" % (start, end if end else -1, multiprocessing.cpu_count()))
  # log_interval = 100
  log_interval = 100
  store = mongo_driver.MongoStore(props.DATASET)
  r_cursor = store.load_raw_stmts(props.TYPE_R, use_normalized=use_normalized)
  r_stmts = []
  for r_stmt in r_cursor:
    if not r_stmt.get('variables', None) or not r_stmt.get('outputs', None):
      continue
    r_stmts.append(r_stmt)
  del r_cursor

  # Top Py Statements
  py_cursor = store.load_raw_stmts(props.TYPE_PYTHON, use_normalized=use_normalized)
  py_stmts = []
  for py_stmt in py_cursor:
    if (not py_stmt.get('variables', None)) or (not py_stmt.get('outputs', None)):
      continue
    py_stmts.append(py_stmt)
  del py_cursor

  for i, r_stmt in enumerate(r_stmts):
    if i < start or (end and i >= end):
      LOGGER.info("Skipping R Stmt: %d / %d !" % (i + 1, len(r_stmts)))
      continue
    existing_diffs = store.load_differences(r_id=r_stmt["_id"])
    processed = set()
    if existing_diffs.count() > skip_threshold:
      LOGGER.info("Processed R Stmt: %d / %d !" % (i + 1, len(r_stmts)))
      continue
    elif existing_diffs.count() > 0:
      for diff in existing_diffs:
        processed.add(diff["py_id"])
    LOGGER.info("Processing R Stmt: %d / %d ... " % (i + 1, len(r_stmts)))
    r_stmt = Statement(mongo_id=r_stmt["_id"], snippet=r_stmt["snippet"],
                       variables=r_stmt["variables"], language=r_stmt["language"],
                       outputs=format_outputs(r_stmt["outputs"]))
    if r_stmt.is_all_same() or r_stmt.is_all_none():
      LOGGER.info("Empty or singular R stmt: %d. Skipping ..." % (i + 1))
      continue
    valid = 0
    took_too_long = 0
    for j in xrange(len(py_stmts)):
      valid += 1
      do_log = valid % log_interval == 0
      py_stmt = py_stmts[j]
      if py_stmt is None:
        if do_log:
          LOGGER.info("Empty or singular py stmt: %d. Skipping ..." % valid)
        continue
      if not isinstance(py_stmt, Statement):
        py_stmts[j] = Statement(mongo_id=py_stmt["_id"], snippet=py_stmt["snippet"],
                                variables=py_stmt["variables"], language=py_stmt["language"],
                                outputs=format_outputs(py_stmt["outputs"]))
        if py_stmts[j].is_all_same() or py_stmts[j].is_all_none():
          py_stmts[j] = None
          if do_log:
            LOGGER.info("Empty or singular py stmt: %d. Skipping ..." % valid)
          continue
        py_stmt = py_stmts[j]
      if py_stmt.mongo_id in processed:
        if do_log:
          LOGGER.info("Already processed py stmt: %d !" % valid)
        continue
      if do_log:
        LOGGER.info("Processing py stmt: %d" % valid)
      difference(r_stmt, py_stmt, store=store, do_log=do_log)
      # prev_signal = signal.getsignal(signal.SIGALRM)
      # signal.signal(signal.SIGALRM, execute.timeout_handler)
      # signal.alarm(max_wait_time)
      # try:
      #   difference(r_stmt, py_stmt, store=store, do_log=do_log)
      # except execute.TimeoutException:
      #   took_too_long += 1
      #   LOGGER.info("Timed out for py: %s" % py_stmt.mongo_id)
      # except Exception as e:
      #   LOGGER.info(e.message)
      # signal.alarm(0)
      # signal.signal(signal.SIGALRM, prev_signal)
    LOGGER.info("# Timed Out for %s = %d" % (r_stmt.mongo_id, took_too_long))


def test_runner():
  args = sys.argv
  start, end = 0, None
  if len(args) >= 3:
    start = int(args[1])
    end = int(args[2])
  elif len(args) >= 2:
    start = int(args[1])
  runner(start=start, end=end, use_normalized=True)


def _test_fetch():
  LOGGER.info("Fetching ... ")
  start = time.time()
  force = do_save = False
  # fetch_statements(props.TYPE_R, force=force, do_save=do_save, limit=None)
  print(len(fetch_statements(props.TYPE_PYTHON, force=force, do_save=do_save, limit=None, as_list=True)))
  end = time.time()
  LOGGER.info("Time Taken: %0.2f" % (end - start))


def test_difference():
  py_id = "5cafffc1e850c97e6a1f9a70"
  r_id = "5cb567d2e850c93c2bec1361"
  store = mongo_driver.MongoStore(props.DATASET)
  start = time.time()
  py_stmt = store.load_stmt(mongo_id=py_id)
  py_stmt = Statement(mongo_id=py_stmt["_id"], snippet=py_stmt["snippet"],
                      variables=py_stmt["variables"], language=py_stmt["language"],
                      outputs=format_outputs(py_stmt["outputs"]))
  py_time = time.time()
  print("Processing Py = %0.2f" % (py_time - start))
  r_stmt = store.load_stmt(mongo_id=r_id)
  r_stmt = Statement(mongo_id=r_stmt["_id"], snippet=r_stmt["snippet"],
                     variables=r_stmt["variables"], language=r_stmt["language"],
                     outputs=format_outputs(r_stmt["outputs"]))
  r_time = time.time()
  print("Processing Py = %0.2f" % (r_time - py_time))
  r_key = r_stmt.outputs.keys()[0]
  py_key = py_stmt.outputs.keys()[0]
  # diffs = compare_returns(r_stmt.outputs[r_key].returns, py_stmt.outputs[py_key].returns)
  # diffs = threaded_compare_returns(r_stmt.outputs[r_key].returns[:4], py_stmt.outputs[py_key].returns[:4])
  diffs = pooled_compare_returns(r_stmt.outputs[r_key].returns, py_stmt.outputs[py_key].returns)
  print(DiffMeta.from_dict(diffs[0].to_dict()))
  end = time.time()
  print("Time Taken = %0.2f" % (end - r_time))
  exit()


if __name__ == "__main__":
  # runner(start=0)
  test_runner()
  # test_difference()
