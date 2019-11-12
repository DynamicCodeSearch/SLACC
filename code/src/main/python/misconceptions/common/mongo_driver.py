import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from bson import ObjectId
import pandas as pd
import pymongo
import rpy2

from utils import logger, lib
from store import mongo_driver
from misconceptions.common import helper, differences

FILE_STMT_COLLECTION = "file_stmts"
STMT_COLLECTION = "stmts"
STMT_NORMALIZED_COLLECTION = "normalized_stmts"
INPUTS_COLLECTIONS = "inputs"
DIFFERENCES_COLLECTIONS = "differences"
SELF_SYNTACTIC_DIFFERENCES_COLLECTION = "self_syntactic_differences"
STMT_FILE_COLLECTION = "stmts_file"

PRIMITIVES = {int, float, str, bool, type(None), list, set, dict, tuple, unicode}
DOT_ESCAPE_CHAR = "|@|"
DOLLAR_ESCAPE_CHAR = "|#|"

LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def mongo_escape(s):
  return s.replace(".", DOT_ESCAPE_CHAR).replace("$", DOLLAR_ESCAPE_CHAR)


def mongo_de_escape(s):
  return s.replace(DOT_ESCAPE_CHAR, ".").replace(DOLLAR_ESCAPE_CHAR, "$")


class MongoStore(lib.O):
  def __init__(self, dataset, **kwargs):
    self.dataset = dataset
    lib.O.__init__(self, **kwargs)

  # File Statements

  def store_file_stmts(self, file_name, snippets, language):
    collection = mongo_driver.get_collection(self.dataset, FILE_STMT_COLLECTION)
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "file_name")
    collection.insert({
      "file_name": file_name,
      "snippets": snippets,
      "language": language
    })

  def load_stmts_for_file_name(self, file_name):
    try:
      return mongo_driver.get_collection(self.dataset, FILE_STMT_COLLECTION).find_one({"file_name": file_name})
    except Exception:
      LOGGER.critical("Failed to load file name : %s" % file_name)
      return None

  def load_file_stmts(self, language=None):
    if language:
      return mongo_driver.get_collection(self.dataset, FILE_STMT_COLLECTION).find({"language": language})
    else:
      return mongo_driver.get_collection(self.dataset, FILE_STMT_COLLECTION).find()

  def delete_file_stmts(self, language=None):
    if language:
      mongo_driver.get_collection(self.dataset, FILE_STMT_COLLECTION).delete_many({"language": language})
    else:
      mongo_driver.get_collection(self.dataset, FILE_STMT_COLLECTION).drop()

  # Statements

  def store_stmt(self, snippet, language, variables):
    collection = mongo_driver.get_collection(self.dataset, STMT_COLLECTION)
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "snippet", "language")
    collection.insert({
      "snippet": snippet,
      "language": language,
      "variables": variables
    })

  def update_stmt_outputs(self, stmt_id, outputs):
    collection = mongo_driver.get_collection(self.dataset, STMT_COLLECTION)
    stmt = collection.find_one({'_id': stmt_id})
    stmt['outputs'] = outputs
    try:
      collection.update_one({'_id': stmt_id}, {"$set": stmt}, upsert=False)
    except Exception:
      stmt['outputs'] = None
      try:
        collection.update_one({'_id': stmt_id}, {"$set": stmt}, upsert=False)
      except Exception as e:
       # import pprint
       # pprint.pprint(outputs[outputs.keys()[0]])
        raise e

  def update_stmt(self, stmt_id, updates):
    collection = mongo_driver.get_collection(self.dataset, STMT_COLLECTION)
    collection.update_one({"_id": stmt_id}, {"$set": updates})

  def load_stmts(self, language=None, is_valid=True, has_output=False, limit=None, use_normalized=False):
    collection_name = STMT_NORMALIZED_COLLECTION if use_normalized else STMT_COLLECTION
    if language:
      stmts = mongo_driver.get_collection(self.dataset, collection_name).find({"language": language})
    else:
      stmts = mongo_driver.get_collection(self.dataset, collection_name).find()
    formatted = {}
    for stmt in stmts:
      if (not is_valid or (is_valid and stmt.get('variables', None))) \
            and (not has_output or (has_output and stmt.get('outputs', None))):
        formatted[(stmt['snippet'], stmt['language'])] = stmt
      if limit and len(formatted) == limit:
        return formatted
    return formatted

  def load_stmt(self, mongo_id, projections=None, use_normalized=False):
    collection_name = STMT_NORMALIZED_COLLECTION if use_normalized else STMT_COLLECTION
    if not isinstance(mongo_id, ObjectId):
      mongo_id = ObjectId(mongo_id)
    return mongo_driver.get_collection(self.dataset, collection_name).find_one({"_id": mongo_id}, projection=projections)

  def load_raw_stmts(self, language=None, use_normalized=False):
    collection_name = STMT_NORMALIZED_COLLECTION if use_normalized else STMT_COLLECTION
    if language:
      return mongo_driver.get_collection(self.dataset, collection_name).find({"language": language})
    else:
      return mongo_driver.get_collection(self.dataset, collection_name).find()

  def load_valid_snippets(self, language=None, use_normalized=False):
    collection_name = STMT_NORMALIZED_COLLECTION if use_normalized else STMT_COLLECTION
    projection = {"outputs": False}
    if language:
      stmts = mongo_driver.get_collection(self.dataset, collection_name).find({"language": language}, projection)
    else:
      stmts = mongo_driver.get_collection(self.dataset, collection_name).find({}, projection)
    valids = []
    for stmt in stmts:
      if stmt.get('variables', None):
        valids.append(stmt)
    return valids

  # Normalized Statements

  def store_normalized_stmt(self, stmt_dict):
    collection = mongo_driver.get_collection(self.dataset, STMT_NORMALIZED_COLLECTION)
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "snippet", "language")
    try:
      collection.insert(stmt_dict, continue_on_error=True)
    except pymongo.errors.DuplicateKeyError as e:
      pass

  # Inputs

  def save_inputs(self, inps):
    collection = mongo_driver.get_collection(self.dataset, INPUTS_COLLECTIONS)
    for inp in inps:
      arg_set = [arg.to_dict(orient='records') for arg in inp]
      collection.insert({
        "args": arg_set
      })

  def delete_inputs(self):
    collection = mongo_driver.get_collection(self.dataset, INPUTS_COLLECTIONS)
    if collection:
      collection.drop()

  def load_inputs(self, column_names):
    collection = mongo_driver.get_collection(self.dataset, INPUTS_COLLECTIONS)
    inps = []
    for inp in collection.find():
      args = []
      for arg in inp["args"]:
        df = pd.DataFrame(arg).reindex(column_names, axis=1)
        args.append(df)
      inps.append(args)
    return inps

  # Stmt File map

  def create_stmt_file_map(self, stmt, stmt_file_map, do_log=True):
    collection = mongo_driver.get_collection(self.dataset, STMT_FILE_COLLECTION)
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_index_for_collection(collection, "snippet")
    try:
      doc = {"snippet": stmt}
      doc.update(stmt_file_map)
      collection.insert(doc)
    except pymongo.errors.DuplicateKeyError as e:
      if do_log:
        LOGGER.warning(e.message)
        LOGGER.info("We continue ... ")

  def load_stmt_file_map(self):
    collection = mongo_driver.get_collection(self.dataset, STMT_FILE_COLLECTION)
    return collection.find()

  # Self Differences

  def save_self_syntactic_difference(self, record, do_log=True):
    collection = mongo_driver.get_collection(self.dataset, SELF_SYNTACTIC_DIFFERENCES_COLLECTION)
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "id_1", "id_2", "language")
      mongo_driver.create_index_for_collection(collection, "d_levenshtein")
      mongo_driver.create_index_for_collection(collection, "d_jaro")
      mongo_driver.create_index_for_collection(collection, "d_jaro_winkler")
      mongo_driver.create_index_for_collection(collection, "d_n_gram")
      mongo_driver.create_index_for_collection(collection, "d_ast")
    try:
      collection.insert(record)
    except pymongo.errors.DuplicateKeyError as e:
      if do_log:
        LOGGER.warning(e.message)
        LOGGER.info("We continue ... ")

  def save_self_syntactic_differences(self, records, do_log=True):
    collection = mongo_driver.get_collection(self.dataset, SELF_SYNTACTIC_DIFFERENCES_COLLECTION)
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "id_1", "id_2", "language")
      mongo_driver.create_index_for_collection(collection, "d_levenshtein")
      mongo_driver.create_index_for_collection(collection, "d_jaro")
      mongo_driver.create_index_for_collection(collection, "d_jaro_winkler")
      mongo_driver.create_index_for_collection(collection, "d_n_gram")
      mongo_driver.create_index_for_collection(collection, "d_ast")
    try:
      collection.insert_many(records)
    except pymongo.errors.DuplicateKeyError as e:
      if do_log:
        LOGGER.warning(e.message)
        LOGGER.info("We continue ... ")

  def load_self_syntactic_differences(self, language=None, id_1=None, id_2=None,
                                      additional_queries=None, projection=None, limit=0):
    collection = mongo_driver.get_collection(self.dataset, SELF_SYNTACTIC_DIFFERENCES_COLLECTION)
    query = {}
    if id_1: query["id_1"] = id_1
    if id_2: query["id_2"] = id_2
    if language: query["language"] = language
    if additional_queries:
      query.update(additional_queries)
    if not limit:
      limit = 0
    return collection.find(query, projection).limit(limit)

  # Cross Differences

  def save_difference(self, r_id, py_id, r_return, py_return, diff, do_log=True):
    collection = mongo_driver.get_collection(self.dataset, DIFFERENCES_COLLECTIONS)
    if not mongo_driver.is_collection_exists(collection):
      mongo_driver.create_unique_index_for_collection(collection, "r_id", "py_id", "r_return", "py_return")
      mongo_driver.create_index_for_collection(collection, "d_levenshtein")
      mongo_driver.create_index_for_collection(collection, "d_jaro")
      mongo_driver.create_index_for_collection(collection, "d_jaro_winkler")
      mongo_driver.create_index_for_collection(collection, "d_n_gram")
      mongo_driver.create_index_for_collection(collection, "d_ast")
    try:
      collection.insert({
        "r_id": r_id,
        "py_id": py_id,
        "r_return": r_return,
        "py_return": py_return,
        "diff": [d.to_dict() if d else None for d in diff]
      })
    except pymongo.errors.DuplicateKeyError as e:
      if do_log:
        LOGGER.warning(e.message)
        LOGGER.info("We continue ... ")

  def difference_exists(self, r_id, py_id, r_return, py_return):
    collection = mongo_driver.get_collection(self.dataset, DIFFERENCES_COLLECTIONS)
    return collection.find_one({"r_id": r_id, "py_id": py_id, "r_return": r_return, "py_return": py_return}) is not None

  def load_difference(self, r_id, py_id, limit=0):
    collection = mongo_driver.get_collection(self.dataset, DIFFERENCES_COLLECTIONS)
    query = {}
    if r_id: query["r_id"] = r_id
    if py_id: query["py_id"] = py_id
    document = collection.find(query).limit(limit)
    docs = []
    for doc in document:
      diff = []
      for d in doc["diff"]:
        if d:
          diff.append(differences.DiffMeta.from_dict(d))
        else:
          diff.append(None)
      doc['diff'] = diff
      doc["r_return"] = doc["r_return"]
      doc["py_return"] = doc["py_return"]
      docs.append(doc)
    return docs

  def load_differences(self, r_id=None, py_id=None, additional_queries=None, projection=None, limit=0):
    collection = mongo_driver.get_collection(self.dataset, DIFFERENCES_COLLECTIONS)
    query = {}
    if r_id: query["r_id"] = r_id
    if py_id: query["py_id"] = py_id
    if additional_queries:
      query.update(additional_queries)
    if not limit:
      limit = 0
    return collection.find(query, projection).limit(limit)

  def update_difference(self, query, updates):
    collection = mongo_driver.get_collection(self.dataset, DIFFERENCES_COLLECTIONS)
    collection.update_many(query, {"$set": updates})

  def delete_differences(self, r_id=None, py_id=None):
    query = {}
    if r_id:
      query["r_id"] = r_id
    if py_id:
      query["py_id"] = py_id
    if not query:
      raise Exception("Empty query. So use drop!")
    LOGGER.info("Deleting differences for query %s .... " % query)
    mongo_driver.get_collection(self.dataset, DIFFERENCES_COLLECTIONS).delete_many(query)

  def delete_difference(self, mongo_id):
    mongo_driver.get_collection(self.dataset, DIFFERENCES_COLLECTIONS).delete_one({"_id": mongo_id})

  def create_semantic_indices(self, indices):
    collection = mongo_driver.get_collection(self.dataset, DIFFERENCES_COLLECTIONS)
    for index in indices:
      mongo_driver.create_index_for_collection(collection, index)

  def load_differences_for_web(self, syn_key, syn_low, syn_high, sim_low, sim_high, limit, allow_size_diff):
    query = {"n_both_empty": {"$eq": 0},
             "semantic_score": {"$gte": sim_low, "$lte": sim_high},
             syn_key: {"$gte": syn_low, "$lte": syn_high}}
    if not allow_size_diff:
      query["$and"] = [{"$or":
                          [{"row_diff": {"$exists": False}}, {"row_diff": {"$eq": 0}}]},
                            {"$or": [{"col_diff": {"$exists": False}}, {"col_diff": {"$eq": 0}}]},
                            {"$or": [{"size_diff": {"$exists": False}}, {"size_diff": {"$eq": 0}}]}]
    print(query)
    diffs = []
    projections = {"py_id": 1,
                   "r_id": 1,
                   "r_snippet": 1,
                   "r_return": 1,
                   "py_return": 1,
                   "py_snippet": 1,
                   "_id": 0,
                   "row_diff": 1,
                   "col_diff": 1,
                   "d_n_gram": 1,
                   "d_ast": 1,
                   "d_levenshtein": 1,
                   "size_diff": 1,
                   "semantic_score": 1}
    for d in self.load_differences(additional_queries=query, projection=projections, limit=limit):
      diffs.append({
        "r_stmt": d["r_snippet"].replace("slacc", "df"),
        "py_stmt": d["py_snippet"].replace("slacc", "df"),
        "d_n_gram": d.get("d_n_gram", None),
        "d_levenshtein": d.get("d_levenshtein", None),
        "d_ast": d.get("d_ast", None),
        "semantic_score": d.get("semantic_score", None),
        "row_diff": d.get("row_diff", None),
        "col_diff": d.get("col_diff", None),
        "size_diff": d.get("size_diff", None)
      })
    return diffs


def to_mongo_format(obj):
  if isinstance(obj, pd.DataFrame):
    obj = obj.where(pd.notnull(obj), None)
    return obj.to_dict(orient='list')
  elif isinstance(obj, pd.Series):
    obj = obj.where(pd.notnull(obj), None)
    return obj.to_list()
  elif type(obj) in PRIMITIVES:
    return obj
  elif type(obj).__module__ == "numpy":
    return getattr(obj, "tolist", lambda x=obj: x)()
  elif isinstance(obj, rpy2.robjects.vectors.ListVector):
    try:
      return helper.convert_r_list_to_py(obj)
    except Exception as e:
      # print obj
      raise e
  raise RuntimeError("Sorry for now we do not support type: %s" % type(obj))
#
#
# def from_mongo_format(obj):
#   if isinstance(obj, pd.DataFrame):
#     return obj.to_dict(into=OrderedDict)
#   raise RuntimeError("Sorry for now we do not support type: %s" % type(obj))


def _test():
  collection = mongo_driver.get_collection("Misconceptions", "differences")
  print(mongo_driver.is_collection_exists(collection))


def _test_stmt_fetch():
  mongo_id = "5cafff91e850c97e6a1f5b9c"
  store = MongoStore("Misconceptions")
  # print(type(mongo_id))
  print(store.load_stmt(mongo_id))


if __name__ == "__main__":
  # _test()
  _test_stmt_fetch()
