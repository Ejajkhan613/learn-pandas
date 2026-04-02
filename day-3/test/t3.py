# 1. Create dataset:
#     - name, marks, salary
#     - Add missing values
#     - Find:
#         - total missing per column
#         - average marks
# 2. Load dataset and print:
#     - shape
#     - dtypes
#     - summary stats
#     - top 5 rows


import pandas as pd

data = {
    "name": ["A", "B", "C", "D", "E","F"],
    "marks": [65, 90, 87, 52, 68, None],
    "salary": [50000, 60000, 55000, None, 52000, 61000]
}

df = pd.DataFrame(data)

print(df.isnull().sum())

print(df["marks"].mean())

print(df.shape)

print(df.dtypes)

print(df.describe())

print(df.head())