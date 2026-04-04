import pandas as pd

data = {
    "name": ["A", "B", "C"],
    "age": [25, 30, 35],
    "salary": [50000.0, 60000.0, 55000.0]
}

df = pd.DataFrame(data)

print(df.dtypes)