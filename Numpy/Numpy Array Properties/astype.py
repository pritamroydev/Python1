import numpy as np

arr = np.array([1,2,3.5, 4])
print(arr.dtype)

int_arr = arr.astype(int)
print(int_arr)
print(int_arr.dtype)