import pandas as pd

data = {
    "date": ["2024-01-01", "2024-02-01"]
}

df = pd.DataFrame(data)

df["date"] = pd.to_datetime(df["date"])

print(df.dtypes)