# 1. Create a DataFrame with columns: `name`, `marks`

import pandas as pd

data = {
    "name": ["a", "b", "c", "d"],
    "marks": [76,87,56,80]
}

dataset = pd.DataFrame(data)

print(dataset)