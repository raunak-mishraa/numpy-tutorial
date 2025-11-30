# Sorting numpy arrays
import numpy as np
arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
# sort the array numerically
print(np.sort(arr)) # [1 2 3 4 5 6 7 8]

# sort the array alphabetically
arr2 = np.array(['banana', 'apple', 'cherry'])
print(np.sort(arr2)) # ['apple' 'banana' 'cherry']

# sort the array of booleans, 0 is False and 1 is True
arr3 = np.array([True, False, True])
print(np.sort(arr3)) # [False  True  True]