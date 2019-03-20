import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from utils import cache, stat, logger
import properties

import json
import re


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))


def coverage(project_name):
  """
  Return coverage for project.
  :param project_name: Name of the project.
  :return: Dictionary with project_name, sloc, lines_covered and code_coverage
  """
  coverage_file = "%s/%s/sloc.json" % (properties.META_RESULTS_FOLDER, project_name)
  json_data = json.loads(cache.read_file(file_name=coverage_file))
  sloc = 0
  lines_covered = 0
  for java_file, stats in json_data.items():
    f_sloc = len(stats["sloc"])
    f_lines_covered = len(stats["linesCovered"])
    sloc += f_sloc
    lines_covered += f_lines_covered
  code_coverage = lines_covered / sloc * 100
  return {
    "project": project_name,
    "sloc": sloc,
    "lines_covered": lines_covered,
    "code_coverage": code_coverage
  }


def _code_jam():
  """
  Run coverage for codejam
  :return:
  """
  codejam_format = r'Y\d+rUtils\d+P\d+'
  total_coverage_percentages = []
  reports = []
  for project_name in sorted(cache.list_dir(properties.META_RESULTS_FOLDER, is_absolute=False)):
    if re.match(codejam_format, project_name):
      LOGGER.info("For project %s" % project_name)
      project_path = "%s/%s" % (properties.META_RESULTS_FOLDER, project_name)
      coverage_percentages = []
      for user in cache.list_dir(project_path, is_absolute=False):
        project_folder = os.path.join(project_name, user)
        metrics = coverage(project_folder)
        coverage_percentages.append(metrics['code_coverage'])
      reports.append("\n### Project: %s" % project_name)
      reports.append(stat.Stat(coverage_percentages).report())
      total_coverage_percentages += coverage_percentages
  LOGGER.info("Aggregating ...")
  reports.append("\n### Total Coverage")
  reports.append(stat.Stat(total_coverage_percentages).report())
  report = "\n".join(reports)
  cache.write_file(os.path.join(properties.RESULTS_FOLDER, "codejam", "coverage.md"), report)
  return report


if __name__ == "__main__":
  _code_jam()
