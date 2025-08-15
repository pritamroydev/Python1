
import pandas as pd

df = pd.read_json("sample_Data.json")

print("Display 10 rows of first: ")
print(df.head(10))          # by default(if no arguments are passed) -> shows first 5 values

print("Display 10 rows of last: ")
print(df.tail(10))          # by default(if no arguments are passed) -> shows last 5 values