# 1. Create a DataFrame and print first 3 rows
# 2. Print last 2 rows
# 3. Print column names

import pandas as pd

data = {
    "name": ["A", "B", "C", "D", "E","F"],
    "age": [25, 30, None, 22, 28, 31],
    "salary": [50000, 60000, 55000, None, 52000, 61000]
}


df = pd.DataFrame(data)

print(df.head(3))

print(df.tail(2))

print(df.columns)