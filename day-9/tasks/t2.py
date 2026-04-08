# 1. Remove spaces from string columns
# 2. Replace `"N/A"` with `None`
# 3. Standardize city names

import pandas as pd

data = {
    "Name": ["John ", "Alice", "JOHN", "Bob", "alice"],
    "Age": [25, 30, 25, None, 30],
    "City": ["DELHI", "Mumbai", "Delhi", "Pune", "N/A"]
}

df = pd.DataFrame(data)

df["Name"] = df["Name"].str.lower().str.strip()

df["City"] = df["City"].replace("N/A", None)

df["City"] = df["City"].str.title()

print(df)