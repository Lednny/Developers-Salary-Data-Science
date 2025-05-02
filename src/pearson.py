from pandas import Series


def valid_cols(col1, col2) -> bool:
    if not isinstance(col1, Series) or not isinstance(col2, Series):
        print("Error: One or both columns are not Series.")
        return False
    return True


class Pearson_Correlation:
    def __init__(self, col1, col2):
        valid_cols(col1, col2)

        self.col1 = col1
        self.col2 = col2


    def calculate(self) -> float:
        return self.col1.corr(self.col2)


    def __str__(self) -> str:
        return f"Pearson Correlation: {self.calculate():.2f}"
