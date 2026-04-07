# 1. Dataset:
#     - age, salary with missing values
#     - Fill:
#         - age → median
#         - salary → mean

import pandas as pd

data = {
    "name": ["A", "B", "C", "D"],
    "age": [25, None, 30, 35],
    "salary": [None, 50000, 54000, 60000]
}

df = pd.DataFrame(data)

med_val = df["age"].median()
mean_val = df["salary"].mean()

df["age"] = df["age"].fillna(med_val)

df["salary"] = df["salary"].fillna(mean_val)

print(df)