from __future__ import print_function, division
import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

HOME = os.getenv("HOME")
ROOT_HOME = os.path.join(HOME, "Raise", "ProgramRepair")
CODESEER_HOME = os.path.join(ROOT_HOME, "CodeSeer")
CODE_HOME = os.path.join(CODESEER_HOME, "code")
META_RESULTS_FOLDER = os.path.join(CODE_HOME, "meta_results")
RESULTS_FOLDER = os.path.join(CODE_HOME, "results")
PROJECTS_HOME = os.path.join(CODESEER_HOME, "projects")
PYTHON_SRC_FOLDER = os.path.join(CODE_HOME, "src", "main", "python")
