# 2. Create a DataFrame and:
#     - Add a new column based on condition (discount if price > 50000)


import pandas as pd

data = {
    "product": ["a", "b", "c", "d"],
    "price": [36000,67000,16000,80000]
}

dataset = pd.DataFrame(data)

dataset["discount"] = dataset["price"] > 50000
print(dataset)