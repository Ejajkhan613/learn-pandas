# 1. Create dataset with missing values and:
#     - Use `.info()`
#     - Count null values
# 2. Use `.describe()` on a dataset and interpret:
#     - mean
#     - min
#     - max

import pandas as pd

data = {
    "name": ["A", "B", "C", "D", "E","F"],
    "age": [25, 30, None, 22, 28, 31],
    "salary": [50000, 60000, 55000, None, 52000, 61000]
}


df = pd.DataFrame(data)

print(df.info())

print(df.isnull().sum())

print(df.describe())

print(df["salary"].mean())

print(df["salary"].min())

print(df["salary"].max())