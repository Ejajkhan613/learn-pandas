import pandas as pd

data = {
    "OrderID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Customer": ["A", "B", "A", "C", "B", "A", "C", "B"],
    "Amount": [250, 450, 300, 200, 500, None, 700, 650],
    "Date": ["2023-01-01", "2023-01-05", "2023-01-07", "2023-01-10",
             "2023-01-15", "2023-01-20", "2023-01-25", "2023-01-30"]
}

df = pd.DataFrame(data)

# Questions:

# 1. Convert Date column to datetime.
# df["Date"] = pd.to_datetime(df["Date"])


# 2. Find total sales.
# print(df["Amount"].sum())


# 3. Find average order amount (ignore missing).
# df.drop_duplicates(inplace=True)
# print(df["Amount"].sum() / df.shape[0])


# 4. Replace missing Amount with median.
# df["Amount"] = df["Amount"].fillna(df["Amount"].median())


# 5. Find total amount spent by each customer.
# print(df.groupby("Customer")["Amount"].sum())


# 6. Find number of orders per customer.
# print(df["Customer"].value_counts())


# 7. Get orders above 400.
# print(df.query("Amount > 400"))


# 8. Sort dataset by Amount.
# print(df.sort_values("Amount",ascending=False))


# 9. Extract month from Date.
# print(pd.to_datetime(df["Date"]).dt.month)


# 10. Filter orders placed after Jan 10.
# df["Date"] = pd.to_datetime(df["Date"])
# print(df[df["Date"] > '2023-01-10'])


# 11. Find highest order per customer.
# print(df.loc[df.groupby("Customer")["Amount"].idxmax()])


# 12. Count how many orders have Amount < 300.
# print(df[df["Amount"] < 300].shape[0])


# 13. Add column "Discounted" (Amount - 10%).
# df["Discount"] = df["Amount"] * 0.90


# 14. Check datatype of all columns.
# print(df.dtypes)


# 15. Drop duplicate customers keeping first occurrence.
# print(df.drop_duplicates(subset="Customer"))