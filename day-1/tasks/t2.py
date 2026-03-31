# 1. Create a Series with custom index `["a", "b", "c"]`

import pandas as pd

data = [5, 10, 15, 20]

dataset = pd.Series(data, index=["a", "b", "c", "d"])

print(dataset)