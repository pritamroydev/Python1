import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Ghanshyam", "Pritam", "Satyam", "Somanth", "Debraj"],
    "Age": [28, 32, 50, 34, 27, 39, 42],
    "Salary": [50000.0, 30000.0, 100000.0, 60000.0, 70000.0, 30000.0, 20000.0],
    "Performance Score": [85, 60, 75, 80, 95, 70, 50]

}

df = pd.DataFrame(data)
print(df)

#df.drop(columns = ["Column_Name"], inplace=True)       -> inplace means it directly modifies the original dataframe

print("\nModified: ")
df.drop(columns= ["Performance Score", "Age"], inplace= True)
print(df)