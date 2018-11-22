import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"


from analysis import arguments
from analysis.helpers import constants as a_consts
from utils import cache
import properties


def get_meta_for_file(file_path):
  args_meta_data = arguments.parse_file_for_args(file_path, properties.CODE_JAM)
  return args_meta_data


def execute(problem_id):
  root_folder = os.path.join(properties.PYTHON_PROJECTS_HOME, problem_id)
  files = []
  for file_path in cache.list_files(root_folder, check_nest=True, is_absolute=True):
    file_name = cache.get_file_name(file_path)
    if file_name == "__init__" or file_name.startswith(a_consts.GENERATED_PREFIX):
      continue
    print(file_path)
    files.append(file_path)
    get_meta_for_file(file_path)


if __name__ == "__main__":
  # get_meta_for_file("/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/python/Y11R5P1/zibada/a.py")
  args = sys.argv
  if len(args) < 2:
    print("Use python codejam/crawl.py <year> <round> <problem_id>")
    exit(0)
  problem_id = args[1]
  execute(problem_id)
