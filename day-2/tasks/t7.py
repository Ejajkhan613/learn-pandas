# 1. Create DataFrame from:
#     
#     [["A", 10], ["B", 20]]
#     
    
#     Then:
    
#     - Rename columns
#     - Change index


import pandas as pd

data = [["A", 10], ["B", 20]]

dataset = pd.DataFrame(data)
dataset.columns = ["name", "age"]
dataset.index = [101, 102]

print(dataset)