# 1. Create DataFrame from list of dicts:
#     - name, salary
# 2. Create DataFrame from NumPy array:
#     - Add column names



import pandas as pd

data = [
    {"name": "aman", "salary": 44593},
    {"name": "raj", "salary": 74593},
    {"name": "ajay", "salary": 54593}
]

dataset = pd.DataFrame(data)

print(dataset)