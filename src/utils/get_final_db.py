from external.json_db_path import get_file_with_saved_path_content
from clear_db import clear_db
from pandas import DataFrame, read_csv
import sys
import os

DB_PATH = get_file_with_saved_path_content()


def get_final_db() -> DataFrame:
    if not DB_PATH or not os.path.exists(DB_PATH):
        print('Not exists DB, Please download with \'download_db.py\' script')
        sys.exit(-1)

    CLEANED_DB_PATH = clear_db(DB_PATH)
    if not CLEANED_DB_PATH: sys.exit(-1)

    DATA = read_csv(CLEANED_DB_PATH)

    return DATA
