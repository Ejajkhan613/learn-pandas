import pandas as pd

data = {
    "name": ["A", "B", "C"],
    "age": [25, None, 30]
}

df = pd.DataFrame(data)

df = df.dropna(axis="columns")

print(df)