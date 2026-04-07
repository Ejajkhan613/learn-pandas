# 1. Drop rows where `age` is missing
# 2. Fill missing `salary` with mean

import pandas as pd

data = {
    "name": ["A", "B", "C", "D"],
    "age": [25, None, 30, 35],
    "salary": [None, 50000, 54000, 60000]
}

df = pd.DataFrame(data)

df = df.dropna(subset="age")

val = df["salary"].mean()

df['salary'] = df['salary'].fillna(val)

print(df)

