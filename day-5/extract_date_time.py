import pandas as pd

data = {
    "date": ["2024-01-01", "2024-02-01"]
}

df = pd.DataFrame(data)

df["date"] = pd.to_datetime(df["date"])

df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day

print(df)