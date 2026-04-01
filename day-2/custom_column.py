import pandas as pd

dataset = pd.DataFrame(
    [[1, 2], [3, 4]],
    index=["row1", "row2"],
    columns=["A", "B"]
)

print(dataset)