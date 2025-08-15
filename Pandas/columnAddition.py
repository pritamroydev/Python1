
"""

"""

import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Ghanshyam", "Pritam", "Satyam", "Somanth", "Debraj"],
    "Age": [28, 32, 50, 34, 27, 39, 42],
    "Salary": [50000.0, 30000.0, 100000.0, 60000.0, 70000.0, 30000.0, 20000.0],
    "Performance Score": [85, 60, 75, 80, 95, 70, 50]

}

df = pd.DataFrame(data)
print(df,"\n")


#syntax:    df["column_name"] = some_value

df["Bonus"] = df["Salary"] * 0.1
print(df)

# using insert() method:    to add column at specific locations
# df.insert(location, "Column_name", some_value)

df.insert(0, "Employee ID", ["001", "002", "003"," 004", "005", "006", "007"])
print(df)

