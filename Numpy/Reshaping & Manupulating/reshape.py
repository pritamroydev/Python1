"""
reshape(rows, columns) specify new shape 
if dimentions match


it doesn't return copy, it returns a view
"""


import numpy as np

arr = np.array([1,2,3,4,5,6])
reshaped_arr = arr.reshape(3,2)
print(reshaped_arr)