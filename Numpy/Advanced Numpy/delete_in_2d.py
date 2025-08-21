
"""
axis = 0 > deletes rows
axis = 1 > deletes columns
"""

import numpy as np

arr = np.array([[10,20,30], [40,50,60], [70,80,90]])
print(arr,"\n")

new_arr = np.delete(arr, 2, axis=0)
print(new_arr,"\n")

new_arr2 = np.delete(arr, 1, axis=1)
print(new_arr2)