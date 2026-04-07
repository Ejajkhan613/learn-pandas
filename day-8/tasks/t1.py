# 1. Create DataFrame with missing values
# 2. Use `isnull()` to detect them
# 3. Count missing values

import pandas as pd

data = {
    "name": ["A", "B", "C"],
    "age": [25, None, 30]
}

df = pd.DataFrame(data)

print(df.isnull())

print(df.isnull().sum())