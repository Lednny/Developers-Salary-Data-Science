from pandas import DataFrame, Series

def main(df: DataFrame, columns: list[str] | None = None) -> int:
    if columns is not None and len(columns) >= 2:
        col1 = df[columns[0]]
        col2 = df[columns[1]]
        if type(col1) == Series and type(col2) == Series:
            correlation = col1.corr(col2, method='pearson')
            print(f"Correlación de Pearson entre '{columns[0]}' y '{columns[1]}': {correlation}")
            return 0
    else:
        print("Correlación de Pearson entre todas las columnas:")
        print(df.corr(method='pearson'))
    return 0
