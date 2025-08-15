
import pandas as pd

data = {
    "Name": ["Ram", "Laxman", "Ghanshyam"],
    "Age": [12, 20, 30],
    "City": ["Andal", "Asansol", "Raniganj"]
}

df = pd.DataFrame(data)

print("Displaying the info. of dataset: ")
print(df.info())