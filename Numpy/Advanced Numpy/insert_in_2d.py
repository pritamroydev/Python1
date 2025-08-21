"""
np.insert(array, index, value, axis=None)
array = original array
index = position at which you want to insert the new element
value = the actual data of the element
axis = (when None, it is for a 1D array)    |   when 0, want to insert row-wise, when 1, want to insert column-wise


returns a copy
"""


import numpy as np

arr_2d = np.array([[1,2,3], 
                   [4,5,6]])
print(arr_2d)

new_arr = np.insert(arr_2d, 1, [10,20,30], axis=0)
print("\n",new_arr)

new_arr2 = np.insert(new_arr, 2, [40,50,60], axis=1)
print("\n",new_arr2)