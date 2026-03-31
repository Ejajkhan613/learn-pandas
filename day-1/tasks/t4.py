# 1. Create a DataFrame:
#     - product, price
#     - Add a new column `tax` = 18% of price

import pandas as pd

data = {
    "product": ["a", "b", "c", "d"],
    "price": [76,87,56,80]
}

dataset = pd.DataFrame(data)

dataset["tax"] = (dataset["price"]/100) * 18
print(dataset)


# 2. Extract only the price column from a DataFrame
print(dataset["price"])