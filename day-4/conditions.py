import pandas as pd

data = {
    "name": ["A", "B", "C", "D", "E"],
    "age": [25, 30, 35, 28, 40],
    "salary": [50000, 60000, 55000, 45000, 70000],
    "city": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"]
}

df = pd.DataFrame(data)

print(df["salary"] > 50000)

print(df.query("salary > 50000"))