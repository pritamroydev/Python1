# syntax -> np.isinf()

import numpy as np

arr = np.array([1,2,np.inf,4,5,-np.inf])
print(np.isinf(arr))
print(arr,"\n")



# how to replace the infinite with finte values

cleaned_arr = np.nan_to_num(arr, posinf=1000, neginf=-1000)
print(np.isinf(cleaned_arr))
print(cleaned_arr)