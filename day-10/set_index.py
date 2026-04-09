import pandas as pd

df = pd.DataFrame({
    "date": ["2024-01-01", "2024-02-01", "2024-03-01"],
    "sales": [100, 200, 150]
})

df["date"] = pd.to_datetime(df["date"])
df = df.set_index(df["date"])

print(df.loc["2024-01-01": "2024-02-01"])