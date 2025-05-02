import pandas as pd
import re

def calculate_salary_mean(salary):
    nums = re.findall(r'\$?(\d+)[Kk]', salario)
    if len(nums) == 2:
        try:
            min_sal = int(nums[0])
            max_sal = int(nums[1])
            return (min_sal + max_sal) / 2 * 1000
        except:
            return None
    return None

def get_salaries_mean(df: pd.DataFrame):
    salaries = df['salary']
    salaries.apply(calculate_salary_mean)
    return salaries