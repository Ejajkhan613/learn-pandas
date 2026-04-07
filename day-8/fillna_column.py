import pandas as pd

data = {
    "name": ["A", "B", "C"],
    "age": [25, None, 30]
}

df = pd.DataFrame(data)

rep_value = df['age'].median()

df = df["age"].fillna(rep_value)

print(df)