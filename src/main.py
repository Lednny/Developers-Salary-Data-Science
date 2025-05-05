from central_tendency import Central_Tendency
from pearson import Pearson_Correlation
from exploratory import Exploratory_Analysis
from utils.get_salaries_mean import get_salaries_mean
from utils.get_final_db import get_final_db
import pandas as pd


def main():
    DATA = get_final_db()

    SALARIES: pd.Series = get_salaries_mean(DATA)

    pearson = Pearson_Correlation(DATA['Company Score'], SALARIES)
    pearson.show_graphics()
    print(pearson.__str__(), end='\n\n')

    central_tendency = Central_Tendency(SALARIES)
    print(central_tendency.__str__(), end='\n\n')

    exploratory = Exploratory_Analysis(DATA)
    print(exploratory.__str__())
    exploratory.run_analysis()


if __name__ == "__main__":
    main()
