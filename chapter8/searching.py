# Searching numpy arrays

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7,4,8, 9])
x = np.where(arr == 4) # gonna return the index of the element
print(x[0]) # (array([3], dtype=int64),) 3 is the index of 4

# Find the indexes where the values are even:
y = np.where(arr%2 == 0)
print(y[0]) # [1 3 5 7]

# Find the indexes where the values are odd:
z = np.where(arr%2 == 1)
print(z[0]) # [0 2 4 6 8 9]

