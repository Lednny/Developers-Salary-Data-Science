import pandas as pd

CLEANED_DB_PATH = "cleaned_db.csv"

def clear_db(DB_PATH: str) -> str | None: # Return the path of the cleaned database
    # pandas.DataFrame.to_csv(df, CLEANED_DB_PATH)
    df = pd.read_csv(DB_PATH)
    df = df.drop_duplicates()
    df = df.dropna()
    df.to_csv(CLEANED_DB_PATH, index=False)
    return CLEANED_DB_PATH
