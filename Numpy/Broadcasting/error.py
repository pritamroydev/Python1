import numpy as np

arr1 = np.array([[1,2,3], [4,5,6]])
arr2 = np.array([1,2])

arr3 = arr1.reshape(3,2)

result = arr3 + arr2
print(result)