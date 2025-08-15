"""
vertically      (Row-wise)
horizontally    (Column-wise)

pd.concate([df1, df2, axis=0, ignore_index=True])

axis= 0,1   -> (row,column wise respectively)

ignore_index = True     -> reset the data for combined df

"""


import pandas as pd

df_Region1 = pd.DataFrame({
    "CustomerId": [1,2],
    "Names": ["Gopal", "Raju"]

})

df_Region2 = pd.DataFrame({
    "CustomerId": [3,4],
    "Names": ["Shyam", "Baburao"]
})


concated_group = pd.concat([df_Region1, df_Region2], axis=1, ignore_index=True)
print(concated_group)