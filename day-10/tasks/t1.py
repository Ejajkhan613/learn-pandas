# 1. Convert a date column to datetime
# 2. Extract year and month
# 3. Print day names

import pandas as pd

df = pd.DataFrame({
    "date": ["2024-01-01", "2024-02-01", "2024-03-01"],
    "sales": [100, 200, 150]
})

df["date"] = pd.to_datetime(df["date"])

print(df["date"].dt.year)
print(df["date"].dt.month)

print(df["date"].dt.day_name())