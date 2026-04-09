import pandas as pd

data = {
    "date": ["2024-01-01", "2024-02-15", "2024-03-10"]
}

df = pd.DataFrame(data)

df["date"] = pd.to_datetime(df["date"], errors="coerce")

print(df["date"].dt.day)
print(df["date"].dt.month)
print(df["date"].dt.year)
print(df["date"].dt.day_of_year)