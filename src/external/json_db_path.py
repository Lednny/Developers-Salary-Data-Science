from os import path
from json import load, dump

FILE_WITH_SAVED_PATH = "db_path.json"


def get_file_with_saved_path_content(OBJ_TO_GET: str = 'PATH') -> str:
    with open(FILE_WITH_SAVED_PATH, 'r') as f:
        JSON_CONTENT = load(f)
        try:
            return JSON_CONTENT[OBJ_TO_GET]
        except Exception:
            return JSON_CONTENT


def saved_db_path_in_file(PATH) -> bool:
    try:
        with open(FILE_WITH_SAVED_PATH, 'w') as f:
            dump({ "PATH": PATH }, f)
        return True
    except Exception:
        return False


def data_set_exists(_PRINT: bool = True) -> bool:
    if path.exists(FILE_WITH_SAVED_PATH):
        DB_PATH = get_file_with_saved_path_content()
        if path.exists(DB_PATH):
            if _PRINT: print(f'DataSet ALREADY EXISTS in {DB_PATH}')
            return True
    return False
