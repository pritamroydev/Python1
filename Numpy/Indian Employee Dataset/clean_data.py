import pandas as pd
import numpy as np

#loading the dataset
df = pd.read_csv(r"C:\Users\user\Desktop\Lang\Python1\Numpy\Indian Employee Dataset\employee_dataset_100_numeric_id_updated.csv")
print(df.head())


#checking the missing values
print("Missing values in each column")
print(df.isnull().sum())

df["Salary(INR)"] = df["Salary(INR)"].fillna(df["Salary(INR)"].mean())
df["Performance Rating"] = df["Performance Rating"].fillna(df["Performance Rating"].median())

#detecting infinite values --> converting them into nan --> then replacing the nan with their mean value
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.fillna(df.mean(numeric_only=True), inplace=True)

#remove duplicate records
df.drop_duplicates(inplace=True)
print(df.head())