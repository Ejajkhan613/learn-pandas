# 1. Filter data for:
#     - dates after "2024-02-01"
# 2. Create column:
#     - weekend or weekday

import pandas as pd

df = pd.DataFrame({
    "date": ["2024-01-01", "2024-02-01", "2024-03-01"],
    "sales": [100, 200, 150]
})

df["date"] = pd.to_datetime(df["date"])

print(df["date"] > "2024-02-01")

df["weekend"] = df["date"].dt.day_of_week

print(df)