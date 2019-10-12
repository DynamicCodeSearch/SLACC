import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

CODE_SRC = os.path.join(os.getenv("HOME"), "Raise/ProgramRepair/CodeSeer/code/src/main")
PROJECTS_SRC = os.path.join(os.getenv("HOME"), "Raise/ProgramRepair/CodeSeer/projects/src/main")
PYTHON_SRC = os.path.join(CODE_SRC, "python")
MISCONCEPTIONS_HOME = os.path.join(PYTHON_SRC, "misconceptions")
RESOURCES_HOME = os.path.join(MISCONCEPTIONS_HOME, "resources")
EXPORT_HOME = os.path.join(os.getenv("HOME"), "Raise/ProgramRepair/CodeSeer/code/meta_results/Misconceptions/exports")
DATASET = "Misconceptions"
TYPE_PYTHON = "py"
TYPE_R = "R"
SELF = "__SELF"
AUTO_RETURN = "__AUTO"
PY_STMT_LIMIT = 5000
