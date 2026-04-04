# 1. Create dataset:
#     - category column
#     - Convert to categorical
#     - Check memory usage (`info()`)

import pandas as pd

data = {
    "city": ["Delhi", "Mumbai", "Delhi", "Pune"]
}

df = pd.DataFrame(data)

print(df.info())

df["city"] = df["city"].astype("category")

print(df.info())