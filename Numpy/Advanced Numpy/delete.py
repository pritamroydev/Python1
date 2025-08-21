"""
np.delete(array, index, axis=None)
flattern array
"""

import numpy as np

arr = np.array([10,20,30,40])
print(arr)

new_arr = np.delete(arr, 2, axis=None)
print(new_arr)