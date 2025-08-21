"""
.insert(array, index, value, axis=None)
array = original array
index = position at which you want to insert the new element
value = the actual data of the element
axis = (when None, it is for a 1D array)    |   when 0, want to insert row-wise, when 1, want to insert column-wise


returns a copy
"""


import numpy as np

arr = np.array([10,20,30,40,60])
print(arr)
new_arr = np.insert(arr, 4, 50, axis=None)
print(new_arr)