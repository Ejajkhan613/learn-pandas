import pandas as pd

data = {
    "name": ["Aman", "Riya", "John", "Sara", "Ali", "Neha"],
    "math": [85, 92, 78, 88, 95, 95],
    "science": [90, 85, 80, 92, 88, 88],
    "english": [78, 88, 85, 90, 92, 92]
}

df = pd.DataFrame(data)

# Information Gathering
print(df.head())
print(df.info())
print(df.describe())

# Total Numbers of each Student
df["total"] = df["math"] + df["science"] + df["english"]

# Average of each Student
df["average"] = df["total"] / 3

# Toppers Filtering
toppers = df[df["average"] > 85]

print(toppers)

# Class Average
class_average = df["average"].mean()

print(class_average)

# Highest Scorer
highest_scorer = df[df["average"] == df["average"].max()]

print(highest_scorer)

# Subject Wise Average
print(df[["math", "english", "science"]].mean())

# Students below 80 average
below = df[df["average"] < 80]

print(below)