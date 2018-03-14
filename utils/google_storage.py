from __future__ import print_function, division
import sys
import os
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "bigfatnoob"

from utils import lib
from google.cloud import storage
from utils.cache import mkdir, file_exists
from joblib import Parallel, delayed
import logging
import csv
import time
from utils.logger import get_logger
from oauth2client.file import Storage
from oauth2client import client
from oauth2client import tools
from apiclient import discovery
import httplib2
from pydrive.auth import GoogleAuth, RefreshError
from pydrive.drive import GoogleDrive
from utils import cache
import argparse


LOG_LEVEL = logging.INFO
logger = get_logger(__name__, LOG_LEVEL)
csv.field_size_limit(sys.maxsize)

# BUCKET_NAME = "enableviz-1380.appspot.com"
BUCKET_NAME = "prog-repair"
BUCKET = None
DRIVE_SECRET_FILE = "secrets/drive_secret.json"
DRIVE_SCOPE = "https://www.googleapis.com/auth/drive"
APPLICATION_NAME = "CodeSeer"
CREDENTIAL_DIR = os.getcwd() + "/secrets"
CREDENTIAL_PATHS = {
    "main": os.path.join(CREDENTIAL_DIR, 'drive_codeseer.json'),
    "george": os.path.join(CREDENTIAL_DIR, 'drive_codeseer_george.json'),
    "rahul": os.path.join(CREDENTIAL_DIR, 'drive_codeseer_rahul.json')
}
GDRIVE_FOLDER_ID = "1cogKeBQ29iNes100sEnG4-CJ2-G2WpqQ"
UPLOADED_FILE_STORE = "data/cfiles_dump/transferred.pkl"
GOOGLE_DRIVE_UPLOADED_FILE_STORE = "data/cfiles_dump/uploaded.pkl"


def get_file_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("-n", "--n_jobs", type=int, default=2, help="Number of jobs")
  parser.add_argument("-o", "--owner", type=str, default="main", help="Owner uploading files")
  return parser.parse_args()


def get_bucket():
  """
  Singleton to return bucket.
  :return:
  """
  global BUCKET
  if BUCKET is None:
    BUCKET = storage.Client().get_bucket(BUCKET_NAME)
  return BUCKET


def get_drive_credentials(owner, flags=None):
  """
  Gets valid user credentials from storage.
  If nothing has been stored, or if the stored credentials are invalid,
  the OAuth2 flow is completed to obtain the new credentials.

  Returns:
      Credentials, the obtained credential.
  """
  if not os.path.exists(CREDENTIAL_DIR):
    os.makedirs(CREDENTIAL_DIR)
  credential_path = CREDENTIAL_PATHS[owner]
  store = Storage(credential_path)
  credentials = store.get()
  if not credentials or credentials.invalid:
    flow = client.flow_from_clientsecrets(DRIVE_SECRET_FILE, DRIVE_SCOPE)
    flow.user_agent = APPLICATION_NAME
    credentials = tools.run_flow(flow, store, flags)
    print('Storing credentials to ' + credential_path)
  return credentials


def implicit():
  """
  Check if client is validly configured
  """
  storage_client = storage.Client()
  # Make an authenticated API request
  buckets = list(storage_client.list_buckets())
  print(buckets)


def get_blob(name):
  """
  Get instance of blob using name from google storage
  :param name:
  :return:
  """
  blob, cnt = None, 0
  while True:
    try:
      blob = storage.Client().get_bucket(BUCKET_NAME).blob(name)
      return blob
    except Exception as e:
      cnt += 1
      if cnt == 10:
        raise e
      time.sleep(60)
      logger.info("Failed to fetch blob from google storage. Sleeping for 1 min")



  return storage.Client().get_bucket(BUCKET_NAME).blob(name)


def download_blob(name, download_path):
  """
  Download a blob from Google Cloud Storage
  :param name: Name of Blob
  :param download_path: Path to be saved
  """
  blob = get_blob(name)
  name = blob.name.rsplit("/", 1)[-1]
  mkdir(download_path)
  if download_path[-1] == "/":
    destination_file = "%s%s" % (download_path, name)
  else:
    destination_file = "%s/%s" % (download_path, name)
  if file_exists(destination_file):
    logger.info("%s already exists" % destination_file)
    return destination_file
  else:
    blob.download_to_filename(destination_file)
    logger.info('Blob {} downloaded to {}.'.format(name, destination_file))
  return destination_file


def download_blobs(prefix_path, download_path, n_jobs, start=0, max_results=None, do_parallel=True):
  """
  :param prefix_path:
  :param download_path:
  :param n_jobs:
  :param max_results:
  :param do_parallel
  :return:
  """
  mkdir(download_path)
  blobs = []
  i = -1
  for stat in get_bucket().list_blobs(prefix=prefix_path):
    i += 1
    if i < start or stat.size == 0:
      continue
    blobs.append(stat.name)
    if max_results is not None and len(blobs) >= max_results:
      break
  print("# Files =", len(blobs))
  if do_parallel:
    Parallel(n_jobs=n_jobs)(delayed(download_blob)(name, download_path) for name in blobs)
  else:
    for name in blobs:
      download_blob(name, download_path)


def list_blobs(prefix_path, max_results=None):
  """
  List all blobs in folder in bucket
  :param prefix_path: Path of the folder
  :param max_results: Max Results to be listed. If None, return all
  :return: List of strings
  """
  blobs = []
  for blob in get_bucket().list_blobs(prefix=prefix_path):
    if blob.size == 0:
      continue
    blobs.append(blob.name)
    if max_results is not None and len(blobs) >= max_results:
      break
  return blobs


def _download_blobs(source, destination, start=0, max_results=None):
  """
  :param source:
  :param destination:
  :param max_results:
  :return:
  """
  n_jobs = 1
  # source, max_results = "pyfiles/csv/", 2
  # source, max_results = "pyfiles/csv_all/", None
  do_parallel = False
  args = sys.argv
  if len(args) >= 2 and lib.is_int(args[1]):
    n_jobs = int(args[1])
    do_parallel = True
  print("Running as %d jobs" % n_jobs)
  download_blobs(source, destination, n_jobs, start, max_results, do_parallel=do_parallel)


def load_drive(owner):
  """
  Load an instance of google drive
  :return:
  """
  gauth = GoogleAuth()
  credential_path = CREDENTIAL_PATHS[owner]
  gauth.LoadCredentialsFile(credentials_file=credential_path)
  if gauth.access_token_expired:
    gauth.Refresh()
  else:
    gauth.Authorize()
  gauth.SaveCredentialsFile(credentials_file=credential_path)
  drive = GoogleDrive(gauth)
  return drive


def upload_file_to_drive(source, destination, folder_id=GDRIVE_FOLDER_ID, owner="main"):
  """
  Upload a file to google drive
  :param source: Name of source
  :param destination: Name of target
  :param folder_id: ID of folder to upload
  :param owner: Owner uploading files to google drive
  :return:
  """
  cnt = 0
  drive = None
  while drive is None:
    try:
      drive = load_drive(owner)
    except RefreshError as e:
      cnt += 1
      drive = None
      logger.info("Failed to fetch access token. Sleeping 3 mins")
      time.sleep(60 * 3)
      if cnt == 10:
        raise e
  splits = destination.rsplit("/", 1)
  file_name = splits[-1]
  gfile = drive.CreateFile({'title': file_name, 'mime_type': 'text/csv',
                            'parents': [{'kind': "drive#fileLink", 'id': folder_id}]})
  gfile.SetContentFile(source)
  cnt = 0
  while True:
    try:
      gfile.Upload()
      break
    except Exception as e:
      cnt += 1
      logger.info("Failed to upload file: %s. Sleeping 3 mins" % file_name)
      time.sleep(60 * 3)
      if cnt == 10:
        raise e
  logger.info("Uploaded file '%s' to google drive" % destination)
  return file_name


def list_file_names():
  """
  List file names from google drive which is saved locally
  :return:
  """
  file_names, cnt = None, 0
  while file_names is None and cnt < 5:
    file_names = cache.load(UPLOADED_FILE_STORE)
    if file_names: return file_names
    time.sleep(60)
    cnt += 1
  if file_names is None:
    raise RuntimeError("File Names is none. Stop and restart")
  return file_names


def save_uploaded_files_to_gdrive(save_file=GOOGLE_DRIVE_UPLOADED_FILE_STORE):
  """
  Save id and title of uploaded files from google drive to a local file
  :param save_file: Local file to save the id and title of files
  """
  drive = load_drive(owner='main')
  file_list = drive.ListFile({'q': "'%s' in parents and trashed=false" % GDRIVE_FOLDER_ID}).GetList()
  file_names = set()
  for g_file in file_list:
    file_names.add((g_file['id'], g_file['title']))
  cache.save(save_file, file_names)


def load_uploaded_files_to_gdrive(save_file=GOOGLE_DRIVE_UPLOADED_FILE_STORE):
  """
  Return id and title as set of tuples uploaded to google drive
  :param save_file: Save file to load data from folder.
  :return: Set of tuples
  """
  return cache.load(save_file)


def transfer_file_from_storage_to_drive(storage_source, local_folder, owner):
  """
  Transfer a file from storage to drive
  :param storage_source: Source of file in google storage
  :param local_folder: Local folder to download the file
  :param owner: Owner uploading files to google drive
  :return:
  """
  uploaded = list_file_names()
  name = storage_source.rsplit("/", 1)[-1].split(".")[0]
  if "%s.csv" % name in uploaded:
    logger.info("%s.csv already processed" % name)
    return
  temp_file = cache.create_file_path(local_folder, name, ext=".tmp")
  if cache.file_exists(temp_file):
    logger.info("%s.csv file being processed" % name)
    return
  cache.save(temp_file, {"processing": True})
  local_file = download_blob(storage_source, local_folder)
  upload_file_to_drive(local_file, local_file, owner=owner)
  uploaded = list_file_names()
  uploaded.add("%s.csv" % name)
  cache.save(UPLOADED_FILE_STORE, uploaded)
  cache.delete(temp_file)
  cache.delete(local_file)


def transfer_from_storage_to_drive(storage_folder, local_folder, owner, n_jobs):
  """
  Transfer all files from google storage to google drive
  :param storage_folder: Google storage folder
  :param local_folder: Local folder where files are temporarily stored
  :param owner: Owner uploading files to google drive
  :param n_jobs: Number of jobs
  :return:
  """
  logger.info("# Jobs = %d" % n_jobs)
  mkdir(local_folder)
  blobs = []
  for stat in get_bucket().list_blobs(prefix=storage_folder):
    if stat.size == 0: continue
    blobs.append(stat.name)
  logger.info("# Files = %d" % len(blobs))
  Parallel(n_jobs=n_jobs)(delayed(transfer_file_from_storage_to_drive)(name, local_folder, owner)
                          for name in blobs)


def download_from_google_drive(file_id, save_path):
  drive = load_drive("main")
  gfile = drive.CreateFile({'id': file_id})
  splits = save_path.rsplit("/", 1)
  if len(splits) > 1: cache.mkdir(splits[0])
  gfile.GetContentFile(save_path)
  logger.info("Downloaded %s to %s" % (gfile['title'], save_path))


def _transfer_from_storage_to_drive():
  _save_uploaded_files()
  args = get_file_args()
  n_jobs = args.n_jobs
  owner = args.owner
  storage_folder = "cfiles"
  local_folder = "data/cfiles_dump/csv_all"
  transfer_from_storage_to_drive(storage_folder, local_folder, owner, n_jobs)


def _list_blobs():
  blob_names = list_blobs("cfiles")
  print(len(blob_names))


def _save_uploaded_files():
  drive = load_drive("main")
  file_list = drive.ListFile({'q': "'%s' in parents and trashed=false" % GDRIVE_FOLDER_ID}).GetList()
  file_names = set()
  for file1 in file_list:
    file_names.add(file1['title'])
  logger.info("# Uploaded Files = %d" % len(file_names))
  cache.save(UPLOADED_FILE_STORE, file_names)


def _save_uploaded_files_to_gdrive():
  save_uploaded_files_to_gdrive('data/cfiles_dump/uploaded.pkl')


def test_google_drive(owner):
  """Shows basic usage of the Google Drive API.

  Creates a Google Drive API service object and outputs the names and IDs
  for up to 10 files.
  """
  flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
  credentials = get_drive_credentials(owner, flags)
  http = credentials.authorize(httplib2.Http())
  service = discovery.build('drive', 'v3', http=http)
  results = service.files().list(pageSize=10, fields="nextPageToken, files(id, name)").execute()
  items = results.get('files', [])
  if not items:
    print('No files found.')
  else:
    print('Files:')
    for item in items:
      print('{0} ({1})'.format(item['name'], item['id']))


if __name__ == "__main__":
  # implicit()
  # _download_blobs("cfiles/csv_all", "data/cfiles_dump/csv_all", start=1, max_results=100)
  # _list_blobs()
  # test_google_drive("rahul")
  # _transfer_from_storage_to_drive()
  _save_uploaded_files_to_gdrive()

