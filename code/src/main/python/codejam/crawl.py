from __future__ import print_function, division
import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from bs4 import BeautifulSoup
import requests
import urllib
import zipfile
import urlparse
import re

from utils import cache, lib, logger
import properties


LOGGER = logger.get_logger(os.path.basename(__file__.split(".")[0]))

DATASET = "CodeJam"
BASE_URL = "http://www.go-hero.net/jam/"
MATCH_STRING = "http://code.google.com/codejam/contest/scoreboard/do?cmd=GetSourceCode"


def crawl_link(url, key):
  LOGGER.info("Fetching URL: %s" % url)
  parsed_url = urlparse.urlparse(url)
  user_name = re.sub('[^a-zA-Z]+', '', urlparse.parse_qs(parsed_url.query)['username'][0])
  user_name_path = os.path.join(properties.PYTHON_PROJECTS_HOME, DATASET, key, user_name)
  cache.mk_package(user_name_path)
  file_handle, _ = urllib.urlretrieve(url)
  zip_file_object = zipfile.ZipFile(file_handle, 'r')
  for file_name in zip_file_object.namelist():
    f = zip_file_object.open(file_name)
    file_path = os.path.join(user_name_path, file_name)
    file_content = f.read()
    cache.write_file(file_path, file_content)
    if not cache.is_valid_python_file(file_path):
      LOGGER.info("Invalid Python File: %s. Deleting it .... " % file_path)
      cache.delete_file(file_path)
  if len(cache.list_files(user_name_path, False, False, ignores=["__init__.py"])) == 0:
    LOGGER.info("Folder '%s' contains no python file. Deleting it")
    cache.delete_folder(user_name_path)


def crawl(year, rnd, problem_id):
  dataset_path = os.path.join(properties.PYTHON_PROJECTS_HOME, DATASET)
  cache.mk_package(dataset_path)
  key = "Y%dR%dP%d" % (year, rnd, problem_id)
  package_path = os.path.join(properties.PYTHON_PROJECTS_HOME, DATASET, key)
  cache.delete_folder(package_path)
  LOGGER.info("Fetching for Year: %d, Round: %d, Problem: %d" % (year, rnd, problem_id))
  cache.mk_package(package_path)
  problem_url = "%s%d/solutions/%d/%d/Python" % (BASE_URL, year, rnd, problem_id)
  page = requests.get(problem_url)
  if page.status_code != properties.SUCCESS_CODE:
    LOGGER.info("Status Code = %s. Unable to fetch page: %s" % (page.status_code, problem_url))
    return
  soup = BeautifulSoup(page.content, 'html.parser')
  for a_tag in soup.find_all('a'):
    if a_tag['href'] and a_tag['href'].startswith(MATCH_STRING):
      crawl_link(a_tag['href'], key)
  LOGGER.info("Completed for Year: %d, Round: %d, Problem: %d\n" % (year, rnd, problem_id))
  # print(soup.prettify())
  # print(page.content)
  # print(problem_url)


def _main():
  args = sys.argv
  if len(args) < 4:
    print("Use python codejam/crawl.py <year> <round> <problem_id>")
    exit(0)
  year = int(args[1])
  rnd = int(args[2])
  problem_id = int(args[3])
  crawl(year, rnd, problem_id)


if __name__ == "__main__":
  _main()
