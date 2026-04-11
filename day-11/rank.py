import pandas as pd

data = {
    "name": ["A", "B", "C", "D", "E"],
    "salary": [50000, 60000, 60000, 45000, 80000],
    "age": [25, 30, 28, 22, 35]
}

df = pd.DataFrame(data)

# df["rank"] = df["salary"].rank()
# df["rank"] = df["salary"].rank(ascending=False)
df["rank"] = df["salary"].rank(ascending=False, method="first").astype(int)

print(df)