from __future__ import print_function, division
import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from utils import cache
from function import Function, Outputs
import properties
import re


def load_functions(class_json_file, project, user):
  class_json = cache.load_json(class_json_file)
  class_name = cache.get_file_name(class_json_file)
  functions = []
  function_pattern = re.compile(r'^func_')
  for function_name, details in class_json.items():
    if not function_pattern.match(function_name):
      continue
    funct = Function(name=function_name, project=project, user=user,
                     class_name=class_name, package="%s.%s" % (project, user),
                     input_key=details["inputKey"], outputs=Outputs(details["outputs"]))
    funct.is_useful()
    functions.append(funct)
  return functions


def load_functions_for_codejam():
  functions = []
  project_pattern = re.compile(r'^Y\d+R\d+P\d+$')
  for project in os.listdir(properties.META_RESULTS_FOLDER):
    if not project_pattern.match(project): continue
    project_folder = os.path.join(properties.META_RESULTS_FOLDER, project)
    for user in os.listdir(project_folder):
      print("%s.%s" % (project, user))
      user_folder = os.path.join(project_folder, user)
      assert os.path.isdir(user_folder)
      for json_file in os.listdir(user_folder):
        if not json_file.endswith(".json"): continue
        functions += load_functions("%s/%s" % (user_folder, json_file), project, user)
  n_valid_functions = 0
  for func in functions:
    if func.is_useful():
      n_valid_functions += 1
  print("Valid Functions : %d / %d" % (n_valid_functions, len(functions)))


# load_functions("/Users/panzer/Raise/ProgramRepair/CodeSeer/code/meta_results/Y14R5P1/Aksenov/generated_class_1fc31152affb49f89695275767decae2.json", "Y14R5P1", "Aksenov")
load_functions_for_codejam()
# print(Outputs(cache.load_json("temp.json").values()[0]['outputs']))
