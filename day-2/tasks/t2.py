# 1. Create a Series with index `["x", "y", "z"]`
import pandas as pd

data = [1,2,3]

dataset = pd.Series(data, index=["x", "y", "z"])

print(dataset)