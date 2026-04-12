import pandas as pd

data = {
    "Name": ["Amit", "Sara", "John", "Priya", "David", "Anita", "Rahul", "Meena"],
    "Math": [78, 85, 96, 67, 89, 73, 88, None],
    "Science": [82, 90, 94, 70, None, 75, 85, 80],
    "English": [74, 88, 92, None, 85, 70, 90, 78],
    "Class": ["A", "A", "B", "B", "A", "B", "A", "B"]
}

df = pd.DataFrame(data)

# ### Questions:

# 1. Display first 3 rows.
# print(df.head(3))

# 2. Show dataset summary including datatypes and non-null counts.
# print(df.dtypes)
# print(df.notnull().sum())


# 3. Find number of missing values in each column.
# print(df.isnull().sum())


# 4. Fill missing values in **Math** with mean.
# mean_val = df['Math'].mean()
# df["Math"] = df["Math"].fillna(mean_val)


# 5. Drop rows where **Science** is missing.
# df = df.dropna(subset="Science")


# 6. Select only students from Class A.
# print(df.query("Class == 'A'"))


# 7. Get students scoring above 85 in Math.
# print(df.query("Math > 85"))


# 8. Find average marks in each subject.
# print(df[["Math", "Science", "English"]].mean())


# 9. Add a column **Total** (sum of all subjects).
# df[["Math", "Science", "English"]] = df[["Math", "Science", "English"]].fillna(0)
# df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
# print(df)


# 10. Find student with highest total score.
# df[["Math", "Science", "English"]] = df[["Math", "Science", "English"]].fillna(0)
# df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
# print(df[df["Total"] == df["Total"].max()])


# 11. Sort students by English marks descending.
# df["English"] = df["English"].fillna(0)
# print(df.sort_values("English", ascending=False))


# 12. Count students in each class.
# print(df["Class"].value_counts())


# 13. Convert Class column to category type.
# df["Class"] = df["Class"].astype("category")
# print(df.dtypes)


# 14. Rename column "Math" to "Mathematics".
# df.rename(columns={"Math": "Mathematics"}, inplace=True)
# print(df)


# 15. Filter students whose English score is between 75 and 90.
# print(df.query("English > 75 and English < 90"))