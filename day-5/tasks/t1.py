# 1. Create DataFrame and check `dtypes`
# 2. Convert integer column to float
# 3. Convert string numbers to integers

import pandas as pd

data = {
    "name": ["A", "B", "C"],
    "age": [25, 30, 35],
    "salary": ["50000", "60000", "55000"]
}

df = pd.DataFrame(data)

print(df.dtypes)

df["age"] = df["age"].astype("float")

df["salary"] = df["salary"].astype("int")

print(df)