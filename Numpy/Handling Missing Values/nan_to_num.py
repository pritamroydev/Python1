# syntax: np.nan_to_num(array, nan=value)   default = 0

import numpy as np

arr = np.array([1,2,np.nan, 4,np.nan, 6])
print(np.isnan(arr))
print(arr,"\n")


cleaned_arr = np.nan_to_num(arr)
print(np.isnan(cleaned_arr))
print(cleaned_arr)

