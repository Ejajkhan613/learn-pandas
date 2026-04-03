# 1. Select column `age`
# 2. Select columns `name` and `city`
# 3. Select first 3 rows using `iloc`

import pandas as pd

data = {
    "name": ["A", "B", "C", "D", "E"],
    "age": [25, 30, 35, 28, 40],
    "salary": [50000, 60000, 55000, 45000, 70000],
    "city": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"]
}

df = pd.DataFrame(data)

print(df["age"])

print(df[["name", "city"]])

print(df.iloc[0:3])