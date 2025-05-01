from external.json_db_path import get_file_with_saved_path_content
from clear_db import clear_db
from central_tendency import central_tendency
import os
import pandas as pd
import sys

DB_PATH = get_file_with_saved_path_content()

def main():
    if not DB_PATH or not os.path.exists(DB_PATH):
        print('Not exists DB, Please download with \'download_db.py\' script')
        sys.exit(-1)

    CLEANED_DB_PATH = clear_db(DB_PATH)
    if not CLEANED_DB_PATH: sys.exit(-1)

    DATA = pd.read_csv(CLEANED_DB_PATH)
    print("DataFrame:\n", DATA.head(10))


if __name__ == "__main__":
    main()

def central_tendency():
    media = serie.mean()
    mediana = serie.median()
    moda = serie.mode()
  return {
        "media": media,
        "mediana": mediana,
        "moda": moda,
  }
