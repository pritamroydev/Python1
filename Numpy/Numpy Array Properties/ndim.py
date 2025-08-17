import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([[1,2,3],[4,5,6]])

arr3 = np.array([[[1,2,3],
                [4,5,6],
                [7,8,9],
                [10,11,12]]])
arr4 = np.array([[[[[[[[[[[[[[[[[[[[[[[[[[[ ]]]]]]]]]]]]]]]]]]]]]]]]]]])

print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim)