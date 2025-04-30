from external.json_db_path import get_file_with_saved_path_content
import os
import pandas as pd
import sys

DB_PATH = get_file_with_saved_path_content()


def main():
    if not DB_PATH or not os.path.exists(DB_PATH):
        print('Not exists DB, Please download with \'download_db.py\' script')
        sys.exit(-1)

    DATA = pd.read_csv(DB_PATH)


if __name__ == "__main__":
    main()
