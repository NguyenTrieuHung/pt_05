
import numpy as np
# 1. Create a numpy array 1D with values between 11 and 101, step by 3.

arr = np.arange(11,102)
#print(arr)

# 2. Extract the values from the numpy array
# Input: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Output: [1, 3, 5, 7, 9]
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
l = arr[1::2]
#print(l)

# 3. Replace the odd values in the numpy array with -1
# Input: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Output: [0, -1, 2, -1, 4, -1, 6, -1, 8, -1]
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
l = arr[1::2]
print(l)

# 4. Reshape/Convert 1D array to 2D array.
# Input: np.arrange(10)
# Output: array with shape (2, 5)

# 5. Stack array x and y vertically (3 ways)
# Input: x = np.arange(10).reshape(2, -1), y = np.repeat(1, 10).reshape(2, -1)

# 6. Stack array x and y horizontally
# Input: x = np.arange(10).reshape(2, -1), y = np.repeat(1, 10).reshape(2, -1)

# 7. Find common values between 2 numpy arrays:
# a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# b = np.array([2, 5, 10, 9, 4, 8, 7, 12])

# 8. Remove all values of array y from array x:
# x = np.array([1, 2, 3, 4, 5, 6])
# y = np.array([2, 5, 3])

# 9. Swap 2 columns/rows in 2D array
# arr = np.arange(9).reshape(3, 3)

# 10. Reverse 2 columns/rows in 2D array
# arr = np.arange(9).reshape(3, 3)
