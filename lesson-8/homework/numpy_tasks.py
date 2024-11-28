import numpy as np
import random

# Task 10., 0., 0., 0.])
# arr1 = np.zeros(10)
# arr1[4] = 1
# print("Task 1:", arr1)

# Task 2
# arr2 = np.arange(10, 50)
# print("Task 2:", arr2)

# Task 3
# arr3 = arr2[::-1]
# print("Task 3:", arr3)

# Task 4
# matrix1 = np.arange(9).reshape(3, 3)
# print("Task 4:\n", matrix1)

# Task 5
# arr4 = np.array([1, 2, 0, 0, 4, 0])
# non_zero_indices = np.nonzero(arr4)[0]
# print("Task 5:", non_zero_indices)

# Task 6
# identity_matrix = np.eye(3)
# print("Task 6:\n", identity_matrix)

# Task 7
# matrix2 = np.random.random((3, 3))
# min_val = np.min(matrix2)
# max_val = np.max(matrix2)
# print("Task 7:\n", matrix2)
# print("Min:", min_val, "Max:", max_val)

# Task 8
# matrix3 = np.random.random((5, 5))
# matrix3_normalized = (matrix3 - np.min(matrix3)) / (np.max(matrix3) - np.min(matrix3))
# print("Task 8:\n", matrix3_normalized)

# Task 9
# arr5 = np.array([1, 3, 5, 11, 15, 20, 25])
# target = 14
# closest_value = arr5[np.abs(arr5 - target).argmin()]
# print("Task 9:", closest_value)

# Task 10
# arr6 = np.array([[5, 9, 3], [10, 2, 15], [6, 7, 8]])
# arr6_modified = arr6.copy()
# for i in range(arr6.shape[0]):
#     arr6_modified[i, np.argmax(arr6[i])] = 0
# print("Task 10:\n", arr6_modified)

# Task 11
# arr7 = np.array([2, 3, 2, 5, 8, 3, 3, 7, 2, 3, 5, 5, 5, 5])
# most_common = np.bincount(arr7).argmax()
# print("Task 11:", most_common)

# Task 12
# arr8 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# matrix_product = np.dot(arr8, arr8.T)
# print("Task 12:\n", matrix_product)

# Task 13
# matrix4 = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
# determinant = np.linalg.det(matrix4)
# print("Task 13: Determinant =", determinant)

# Task 14
# matrix5 = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
# try:
#     matrix_inverse = np.linalg.inv(matrix5)
#     print("Task 14:\n", matrix_inverse)
# except np.linalg.LinAlgError:
#     print("Task 14: Matrix is singular and cannot be inverted.")
