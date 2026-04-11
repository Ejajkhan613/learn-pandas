import pandas as pd

data = {
    "name": ["A", "B", "C", "D", "E"],
    "salary": [50000, 70000, 60000, 45000, 80000],
    "age": [25, 30, 28, 22, 35]
}

df = pd.DataFrame(data)

# df = df.sort_values(by="salary")
df = df.sort_values(by=["salary", "age"])

print(df)