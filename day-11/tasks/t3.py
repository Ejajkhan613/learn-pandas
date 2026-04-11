# 1. Rank students by marks (highest = rank 1)
# 2. Sort dataset and:
#     - assign rank
#     - extract top 5
# 3. Handle ties using:
#     - `dense` ranking

import pandas as pd

data = {
    "name": ["A", "B", "C", "D", "E"],
    "marks": [65, 87, 45, 78, 60],
    "age": [25, 30, 28, 22, 35]
}

df = pd.DataFrame(data)

df["rank"] = df["marks"].rank(ascending=False, method="dense").astype(int)

df = df.sort_values(by="rank")

print(df.head())