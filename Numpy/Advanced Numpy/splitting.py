"""
np.split(arr, parts) > equal split

"""

import numpy as np

arr1 = np.array([10,20,30,40,50,60])

print(np.split(arr1, 2),"\n")


"""
for 2d:
np.vsplit()
np.hsplit()

"""

arr2 = np.array([[1,2,3,0], [4,5,6,0], [7,8,9,0]])
print(arr2,"\n")

print(np.vsplit(arr2, 3),"\n")

print(np.hsplit(arr2, 2))