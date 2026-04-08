# 1. Rename columns to lowercase
# 2. Convert names to lowercase
# 3. Remove duplicate rows

import pandas as pd

data = {
    "User Name": ["John ", "Alice", "JOHN", "Bob", "alice"],
    "Age": [25, 30, 25, None, 30],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Unknown"]
}

df = pd.DataFrame(data)

df = df.rename(columns={
    "User Name": "names",
    "Age": "age",
    "City": "city"
})


df["names"] = df["names"].str.lower().str.strip()

df = df.drop_duplicates()

print(df)