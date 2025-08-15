
# pd.merge(df1, df2, on="Column Name", how="type of join")

import pandas as pd

#customer dataframe
df_customer = pd.DataFrame({
    "CustomerId": [1,2,3],
    "Name": ["Ramesh", "Suresh", "Mahesh"],

})

#order dafaframe
df_order = pd.DataFrame({
    "CustomerId": [1,2,4],
    "OrderAmount": [250, 450, 350]
})

#merge
# df_merge = pd.merge(df_customer, df_order, on="CustomerId", how="left")

# df_merge = pd.merge(df_customer, df_order, on="CustomerId", how="right")

# df_merge = pd.merge(df_customer, df_order, on="CustomerId", how="inner")

# df_merge = pd.merge(df_customer, df_order, on="CustomerId", how="outer")


df_merge = pd.merge(df_customer, df_order, how="cross")
print(df_merge)
print("\n")