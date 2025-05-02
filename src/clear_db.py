from sys import argv as ARGS
import pandas as pd
import os

CLEANED_DB_PATH = "cleaned_db.csv"
FLAGS = { "clear": bool("--not-clear" in ARGS) }

def clear_db(DB_PATH: str) -> str | None: # Return the path of the cleaned database
    if os.path.exists(CLEANED_DB_PATH):
        if FLAGS["clear"] or input('CLEANDED DB ALREADY EXISTS, DO YOU WANT TO UPDATE or RESTORE [Y/n]? ').lower() != 'y':
            return CLEANED_DB_PATH
        else:
            os.remove(CLEANED_DB_PATH)

    print("Cleaning DataSet...")
    df = pd.read_csv(DB_PATH)
    df = df.drop_duplicates()
    df = df.dropna()
    df['Company Score'] = pd.to_numeric(df['Company Score'], errors='coerce')
    df.to_csv(CLEANED_DB_PATH, index=False)
    print("Done!\n")
    return CLEANED_DB_PATH
