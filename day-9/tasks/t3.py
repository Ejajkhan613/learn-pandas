# 1. Dataset:
#     - Duplicate names (case + spaces issue)
#     - Clean and deduplicate
# 2. Create cleaning pipeline:
#     - Rename columns
#     - Clean strings
#     - Handle missing values
# 3. Replace:
#     - invalid values with mean


import pandas as pd

data = {
    "Name": ["John ", "Alice", "JOHN", "Bob", "alice"],
    "Age": [25, 30, 25, None, 30],
    "City": ["DELHI", "Mumbai", "Delhi", "Pune", "N/A"]
}

df = pd.DataFrame(data)


df["Name"] = df["Name"].str.lower().str.strip()

df["City"] = df["City"].str.title()

df = df.drop_duplicates()

df.columns = ["Names", "Ages", "Cities"]

df["Ages"] = df["Ages"].fillna(df["Ages"].mean())

df["Cities"] = df["Cities"].str.replace({"N/A": "Bangalore"})

print(df)