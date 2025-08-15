import pandas as pd

#reading data from CSV file into a dataframe
#encoding are of 2 types: utf-8, latin1

rcsv = pd.read_csv("sales_data_sample.csv", encoding="latin1")
# print(rcsv)


rxls = pd.read_excel(r"SampleSuperstore.xlsx")
# print(rxls)

rjson = pd.read_json("sample_Data.json")
print(rjson)