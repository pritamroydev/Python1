
"""
axis = 0 > vertical stacking
axis = 1 > horizontal stacking

"""

import numpy as np

arr = np.array([10,20,30]).reshape(1,3)

arr2 = np.array([40,50,60]).reshape(1,3)

new_arr = np.concatenate((arr, arr2), axis=0)
new_arr2 = np.concatenate((arr2, arr), axis=1)

print(new_arr)
print(new_arr2)
