# 1. Create dataset:
#     - price (string), date (string)
#     - Convert both correctly
#     - Calculate average price


import pandas as pd

data = {
    "date": ["2024-01-01", "2024-02-01"],
    "price": ["500", "600"]
}

df = pd.DataFrame(data)

df["date"] = pd.to_datetime(df["date"])

df["price"] = df["price"].astype("int")


print(df)