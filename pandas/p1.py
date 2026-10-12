import pandas as pd


data = {
    "Name": ["Rahul", "Priya", "Arun"],
    "Age": [25, 28, 24],
    "Salary": [50000, 65000, 45000]
}

df = pd.DataFrame(data)

print(df)
print(type(df))
print(df.shape)
print(df.columns)
print(df["Name"])
print(type(df["Name"]))
print(df["Salary"])
print(df[["Name", "Age"]])
print(df[df["Age"]>24])
print(df[df["Salary"]> 50000])
print(df[df["Age"] <=25])
print(df[(df["Age"] > 24) & (df["Salary"] > 50000)])
print(df[(df["Age"] < 25) | (df["Salary"] > 50000)])