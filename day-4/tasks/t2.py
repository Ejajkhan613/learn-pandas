# 1. Select rows where salary > 55000
# 2. Select rows where city = "Delhi"
# 3. Select only `name` and `salary` where salary > 50000

import pandas as pd

data = {
    "name": ["A", "B", "C", "D", "E"],
    "age": [25, 30, 35, 28, 40],
    "salary": [50000, 60000, 55000, 45000, 70000],
    "city": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"]
}

df = pd.DataFrame(data)

print(df.query("salary > 55000"))

print(df[df["city"] == "Delhi"])

print(df[df["salary"] > 50000][["name", "salary"]])