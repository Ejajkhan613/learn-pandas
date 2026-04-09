# 1. Dataset:
#     - date, sales
#     - Extract month
#     - Calculate monthly sales
# 2. Set date as index and:
#     - slice data for a specific range
# 3. Handle invalid dates using `errors="coerce"`

import pandas as pd

df = pd.DataFrame({
    "date": ["2024-01-01", "2024-02-01", "2024-03-01"],
    "sales": [100, 200, 150]
})

df["date"] = pd.to_datetime(df["date"], errors="coerce")

df["month"] = df["date"].dt.month

print(df.groupby("month")["sales"].sum())


df = df.set_index("date")

print(df.loc["2024-01-01": "2024-02-01"])
