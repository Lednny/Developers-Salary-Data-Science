from src.external.json_db_path import data_set_exists, saved_db_path_in_file
import kagglehub
import sys

if data_set_exists():
    sys.exit(0)

# Download latest version
DATA_SET = "emreksz/software-engineer-jobs-and-salaries-2024"
PATH = kagglehub.dataset_download(DATA_SET)

if saved_db_path_in_file(PATH):
    print(f'DataSet DOWNLOADED in {PATH}')
else:
    print('ERROR, NOT DOWNLOADED :(')
