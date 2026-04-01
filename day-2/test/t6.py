# 1. Create DataFrame:
#     - name, marks
#     - Custom index as student IDs

import pandas as pd

data = {
    "name": ["rahul", "ajay", "anuj", "suraj"],
    "marks": [76, 64, 99, 82]
}

dataset = pd.DataFrame(data, index=[101,102,103,104])

print(dataset)