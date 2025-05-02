from external.json_db_path import get_file_with_saved_path_content
from clear_db import clear_db
from central_tendency import Central_Tendency
from pearson import Pearson_Correlation
from utils.get_salaries_mean import get_salaries_mean
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


    SALARIES: pd.Series = get_salaries_mean(DATA)

    pearson = Pearson_Correlation(DATA['Company Score'], SALARIES)
    print(pearson.__str__(), end='\n\n')

    central_tendency = Central_Tendency(SALARIES)
    print(central_tendency.__str__(), end='\n\n')


if __name__ == "__main__":
    main()
