import pandas as pd

data = {
    "User Name": ["JOHN", "Alice", "JOHN", "Bob", "alice"],
    "Age": [25, 30, 25, None, 30],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"]
}

df = pd.DataFrame(data)

df.columns = ["User", "Umar", "Shahar"]

print(df)