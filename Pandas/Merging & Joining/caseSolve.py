
import pandas as pd

df_customerProfile = pd.DataFrame({
    "CustomerId": [1,2,3],
    "Name": ["Pritam", "Saytam", "Shiva"]
})

df_transactions = pd.DataFrame({
    "CustomerId": [1,2,3],
    "Transactions": [2500, 3000, 1500]
})


mergedGroup = pd.merge(df_customerProfile, df_transactions, on="CustomerId", how="inner")
print("\nMerged Group:")
print(mergedGroup)

df_newCustomer = pd.DataFrame({
    "CustomerId": [4],
    "Name": ["Vishnu"],
    "Transactions": [6000]
})

concateGrp = pd.concat([mergedGroup, df_newCustomer], axis=0, ignore_index=True)
print("\nConcatinated Group: ")
print(concateGrp)

