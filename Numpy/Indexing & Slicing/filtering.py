
#filtering / boolean masking -> it is filtering the data of an array on conditional basis (much faster than loops)

import numpy as np

arr = np.array([10,20,30,40,50,60])

print(arr[arr>25])