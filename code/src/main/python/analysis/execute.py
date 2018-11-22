import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

import properties
import imp



def execute_file(file_name):
  sys.path.append(properties.PYTHON_PROJECTS_HOME)
  python_name = file_name.split(properties.PYTHON_PROJECTS_HOME)[-1][1:].split(".")[0].replace(os.path.sep, ".")
  print(python_name)
  module = __import__('Y11R5P1.dennislissov.A')
  print(dir(module))
  # print(getattr(getattr(module, "dummy"), "func_a"))
  # print(imp.find_module("stupid.dummy"))
  # print(imp.find_module('stupid.dummy', [properties.PYTHON_PROJECTS_HOME+'/']))
  # print(imp.load_source("*", "./stupid/generated_py_2e91a2b94d274665a8a640e0fe522d0e.py"))


# execute_file("/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/python/stupid/generated_py_2e91a2b94d274665a8a640e0fe522d0e.py")


