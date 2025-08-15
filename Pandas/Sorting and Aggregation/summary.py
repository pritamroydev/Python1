"""
df["Column Name"].mean()
df["Column Name"].sum()
df["Column Name"].min()
df["Column Name"].max()

"""


import pandas as pd


data = {
    "Name": ["Ram", None, "Shyam", "Ghanshyam", "Pritam", "Satyam", "Somanth", "Debraj"],
    "Age": [28, None, 32, 50, 34, 27, 39, 42],
    "Salary": [50000.0, None, 30000.0, 100000.0, 600000, 70000.0, 30000.0, 20000.0],
    "Performance Score": [85, None, 60, 75, 80, 95, 70, 50]

}

df = pd.DataFrame(data)

print(f"\nTotal Sum of Salary given: {df["Salary"].sum()}")