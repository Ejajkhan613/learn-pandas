# 1. Create dataset:
#     - city column → convert to category
# 2. Create date column:
#     - Convert to datetime
#     - Extract year

import pandas as pd

data = {
    "city": ["Delhi", "Mumbai"],
     "date": ["2024-01-01", "2024-02-01"]
}

df = pd.DataFrame(data)

df['city'] = df['city'].astype('category')

df['date'] = pd.to_datetime(df['date'])

df["year"] = df["date"].dt.year


print(df)