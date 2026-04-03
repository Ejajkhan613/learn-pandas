# 1. Create DataFrame from NumPy array:
#     - Add column names



import pandas as pd
import numpy as np

data = np.array([["A"], ["B"],["C"]])

dataset = pd.DataFrame(data)
dataset.columns = ["name"]

print(dataset)