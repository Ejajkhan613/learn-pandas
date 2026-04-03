# 1. Create a DataFrame with columns:
#     - `city`, `population`

import pandas as pd

data = {
    "city": ["delhi", "mumbai", "chennai", "kolkata"],
    "population": [543324,343345,34353,64543]
}

dataset = pd.DataFrame(data)

print(dataset)