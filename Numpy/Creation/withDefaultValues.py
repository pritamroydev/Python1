#with default values

#--------------------------------------------------------

#syntax: np.zeros(shape)    (3)     - for 1D
#                           ([3,3])   - for 2D
#np.zeroes  -> fills the array by default values 0

import numpy as np

array = np.zeros([3, 3])

print(array)
print("\n")

#--------------------------------------------------------

#syntax: np.ones(shape)     (3)     - for 1D
#                           ([3,3])   - for 2D
#np.ones  -> fills the array by default values 1


array2 = np.ones([4,4])
print(array2)
print("\n")

#--------------------------------------------------------


#syntax: np.full(shape, value)    (3)     - for 1D
#                           ([3,3])   - for 2D
#np.full  -> fills the array by desired default values

array3 = np.full([3,3], 7)
print(array3)