# 1. Sort by:
#     - age ascending
#     - salary descending
# 2. Find top 3 highest salaries

import pandas as pd

data = {
    "name": ["A", "B", "C", "D", "E"],
    "salary": [50000, 60000, 60000, 45000, 80000],
    "age": [25, 30, 28, 22, 35]
}

df = pd.DataFrame(data)

df = df.sort_values(by="age")
df = df.sort_values(by="salary", ascending=False)

print(df.head(3))