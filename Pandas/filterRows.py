
import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Ghanshyam", "Pritam", "Satyam", "Somanth", "Debraj"],
    "Age": [28, 32, 50, 34, 27, 39, 42],
    "Salary": [50000.0, 30000.0, 100000.0, 60000.0, 70000.0, 30000.0, 20000.0],
    "Performance Score": [85, 60, 75, 80, 95, 70, 50]

}


df = pd.DataFrame(data)

# single condition
column1 = df[df["Salary"]>50000]
print(f"\nSalary > 50000: \n{column1}")


# multiple condition
column2 = df[(df["Salary"]>50000) & (df["Age"]>30)]
print(f"\nSalary > 50000 and Age > 30: \n{column2}")


# using OR condition
column3 = df[(df["Age"]>30) | (df["Performance Score"]>90)]
print(f"\nAge > 30 or Performance score > 90: \n{column3}")