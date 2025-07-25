from os import path
from json import load, dump

FILE_WITH_SAVED_PATH = "db_path.json"


def get_file_with_saved_path_content(OBJ_TO_GET: str = 'PATH') -> str | None:
    try:
        with open(FILE_WITH_SAVED_PATH, 'r') as f:
            JSON_CONTENT = load(f)
            try:
                return JSON_CONTENT[OBJ_TO_GET]
            except Exception:
                return None
    except Exception:
        return None


def saved_db_path_in_file(PATH, CSV_FILE: str = "Software Engineer Salaries.csv") -> bool:
    ULT_PATH = path.join(PATH, CSV_FILE)
    try:
        with open(FILE_WITH_SAVED_PATH, 'w') as f:
            dump({ "PATH": ULT_PATH }, f)
        return True
    except Exception:
        return False


def data_set_exists(_PRINT: bool = True) -> bool:
    if path.exists(FILE_WITH_SAVED_PATH):
        DB_PATH = get_file_with_saved_path_content()
        if not DB_PATH: return False
        if path.exists(DB_PATH):
            if _PRINT: print(f'DataSet ALREADY EXISTS in {DB_PATH}')
            return True
    return False
