
import pandas as pd

data = {
    "Name": ["Ram", "Laxman", "Ghanshyam"],
    "Age": [12, 20, 30],
    "City": ["Andal", "Asansol", "Raniganj"]
}

df = pd.DataFrame(data)
print(df)

df.to_csv("output.csv", index=False)    # index=False -> cleans the index values
print("CSV file saved...")

df.to_excel("output.xlsx", index=False)
print("Excel file saved...")

df.to_json("output.json", index=False)
print("JSON file saved...")