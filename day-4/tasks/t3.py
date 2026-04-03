# 1. Filter:
#     - age > 30 AND salary > 50000
# 2. Use `query()` to:
#     - get employees from Mumbai with salary > 60000
# 3. Select:
#     - first 3 rows
#     - only columns name & age
        
#         using `loc`


import pandas as pd

data = {
    "name": ["A", "B", "C", "D", "E"],
    "age": [25, 30, 35, 28, 40],
    "salary": [50000, 60000, 55000, 45000, 70000],
    "city": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"]
}

df = pd.DataFrame(data)

print(df.query("age > 30 & salary > 50000"))

print(df.query("city > 'Mumbai' & salary > 50000"))

print(df.loc[0:2, ["name", "age"]])