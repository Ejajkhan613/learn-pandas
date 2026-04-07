# 1. Apply:
#     - forward fill on time-series-like data
# 2. Compare:
#     - original vs cleaned dataset

import pandas as pd

data = {
    "day": [1, 2, 3, 4, None, None, 7, 8]
}

df = pd.DataFrame(data)

print(df["day"].ffill())

print(df)