import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from analysis.helpers import constants as a_consts
from analysis import generate
from utils import cache
import properties


def execute(problem_id):
  root_folder = os.path.join(properties.PYTHON_PROJECTS_HOME, problem_id)
  for file_path in cache.list_files(root_folder, check_nest=True, is_absolute=True):
    file_name = cache.get_file_name(file_path)
    if file_name == "__init__" or file_name.startswith(a_consts.GENERATED_PREFIX):
      continue
    generate.generate_for_file(properties.CODE_JAM, file_path)


if __name__ == "__main__":
  args = sys.argv
  if len(args) < 2:
    print("Use python codejam/file_meta_data.py <problem_id>")
    exit(0)
  execute(args[1])
