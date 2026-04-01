import pandas as pd

data = [
    {"user": "A", "score": 90},
    {"user": "B", "score": 80}
]

dataset = pd.DataFrame(data)

print(dataset)