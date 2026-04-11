# 1. Sort dataset by age
# 2. Sort salary in descending order
# 3. Sort index

import pandas as pd

data = {
    "name": ["A", "B", "C", "D", "E"],
    "salary": [50000, 60000, 60000, 45000, 80000],
    "age": [25, 30, 28, 22, 35]
}

df = pd.DataFrame(data)

df = df.sort_values(by="age")

df = df.sort_values(by="salary")

df = df.sort_index()