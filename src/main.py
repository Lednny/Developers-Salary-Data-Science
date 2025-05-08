from central_tendency import Central_Tendency
from pearson import Pearson_Correlation
from binary_regresion import Binary_Regression
from exploratory import Exploratory_Analysis
from linear_regression import Linear_Regression
from utils.get_salaries_mean import get_salaries_mean
from utils.get_final_db import get_final_db
import pandas as pd


def main():
    DATA: pd.DataFrame = get_final_db()

    SALARIES: pd.Series = get_salaries_mean(DATA)

    pearson = Pearson_Correlation(DATA['Company Score'], SALARIES)
    pearson.show_graphics()
    pearson.show_heat_map()
    print(pearson.__str__(), end='\n\n')

    binary_regression = Binary_Regression(DATA)
    binary_regression.show_graphics()
    print(binary_regression.__str__(), end='\n\n')

    central_tendency = Central_Tendency(SALARIES)
    print(central_tendency.__str__(), end='\n\n')

    exploratory = Exploratory_Analysis(DATA)
    print(exploratory.__str__())
    print(exploratory.run_analysis())

    linear_regression = Linear_Regression(DATA)
    print(linear_regression.__str__())
    linear_regression.show_graphics()


if __name__ == "__main__":
    main()
