
import pandas as pd

data = {
    "Name": ["Arun", "Karun", "Varun", "Marun", "Narun"],
    "Age": [24, 32, 28, 32, 24],
    "Salary": [25000, 32000, 45000, 54000, 34000]

}

df = pd.DataFrame(data)
grouped = df.groupby(["Age", "Name"])["Salary"].sum()
print(grouped)