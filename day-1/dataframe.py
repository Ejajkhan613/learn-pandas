import pandas as pd

data = {
    "name": ["rahul", "ajay", "anuj", "suraj"],
    "age": [26, 14, 29, 32]
}

dataset = pd.DataFrame(data)

print(dataset)