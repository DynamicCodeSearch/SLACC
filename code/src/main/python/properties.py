import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

"""
File paths
"""
HOME = os.getenv("HOME")
ROOT_HOME = os.path.join(HOME, "Raise", "ProgramRepair")
CODESEER_HOME = os.path.join(ROOT_HOME, "SLACC")
CODE_HOME = os.path.join(CODESEER_HOME, "code")
META_RESULTS_FOLDER = os.path.join(CODE_HOME, "meta_results")
META_STORE_FOLDER = os.path.join(CODE_HOME, "meta_store")
RESULTS_FOLDER = os.path.join(CODE_HOME, "results")
PROJECTS_HOME = os.path.join(CODESEER_HOME, "projects")
PYTHON_SRC_FOLDER = os.path.join(CODE_HOME, "src", "main", "python")
ARGUMENTS_FOLDER = os.path.join(META_STORE_FOLDER, "%s", "arguments")
ARGUMENTS_INDEX_JSON = os.path.join(ARGUMENTS_FOLDER, "index.json")
FUNCTIONS_META_FOLDER = os.path.join(META_STORE_FOLDER, "%s", "functions")
FUNCTIONS_RESULTS_FOLDER = os.path.join(META_RESULTS_FOLDER, "%s", "functions")
CLUSTERS_FOLDER = os.path.join(META_RESULTS_FOLDER, "%s", "clusters")


PYTHON_PROJECTS_HOME = os.path.join(PROJECTS_HOME, "src", "main", "python")

"""
Constants
"""
FUZZ_ARGUMENT_SIZE = 256
SUCCESS_CODE = 200
CODE_JAM = "codejam"
INTRO_CLASS_JAVA = "introclass"
MIN_STATEMENT_SIZE = 2

"""
Config
"""
STORE = "mongo"  # Can be "json"/"mongo"
CLUSTER_TYPE = "representative"  # Can be "representative"/"dbscan"
