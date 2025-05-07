from pandas import DataFrame, Series
import re


def calculate_salary_mean(salary) -> float:
    if not isinstance(salary, str):
        return 0

    nums = re.findall(r'\$?(\d+)[Kk]', salary)

    if len(nums) == 2:
        try:
            min_sal = int(nums[0])
            max_sal = int(nums[1])
            return (min_sal + max_sal) / 2

        except:
            return 0

    elif len(nums) == 1:
        try:
            return int(nums[0])

        except:
            return 0

    return 0


def get_salaries_mean(df: DataFrame, col: str = 'Salary') -> Series:
    salaries = df[col]

    if not isinstance(salaries, Series):
        raise ValueError("Input data must be a pandas Series")

    new_salaries = salaries.apply(calculate_salary_mean)

    if not isinstance(new_salaries, Series):
        raise ValueError("Input data must be a pandas Series")

    return new_salaries
