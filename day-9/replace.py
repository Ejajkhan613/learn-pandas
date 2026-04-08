import pandas as pd

data = {
    "User Name": ["John ", "Alice", "JOHN", "Bob", "alice"],
    "Age": [25, 30, 25, None, 30],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Unknown"]
}

df = pd.DataFrame(data)

df["User Name"] = df["User Name"].replace({"JOHN": "Jonny"})

print(df)