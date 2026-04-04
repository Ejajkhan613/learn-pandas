import pandas as pd

data = {
    "city": ["Delhi", "Mumbai", "Delhi", "Pune"]
}

df = pd.DataFrame(data)

df["city"] = df["city"].astype("category")

print(df.dtypes)