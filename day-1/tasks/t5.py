# 1. Create a DataFrame of 5 students:
    # - name, marks
    # - Add a column `pass` (True if marks > 40)

import pandas as pd

data = {
    "name": ["a", "b", "c", "d"],
    "marks": [36,87,56,80]
}

dataset = pd.DataFrame(data)
dataset["pass"] = dataset["marks"] > 40

print(dataset)