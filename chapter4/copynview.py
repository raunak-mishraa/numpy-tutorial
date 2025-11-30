import numpy as np
# Copy and View

# View , jab bhi original array change hota hai to view bhi change hota hai something like reference, if you change the view then original array will also change, they are sharing the same memory
arr = np.array([1, 2, 3, 4, 5])

# create a view
arr_view = arr.view()

print(f'Original array: {arr}')
print(f'View of original array: {arr_view}')

# Change the array
arr[0] = 10

print(f'Original array after change: {arr}')
print(f'Original View : {arr_view}')

# Copy, jab bhi original array change hota hai to copy nahi hota
arr = np.array([1, 2, 3, 4, 5])

# create a copy
arr_copy = arr.copy()

print(f'Original array: {arr}')
print(f'Copy of original array: {arr_copy}')

# Change the array
arr[0] = 10

print(f'Original array after change: {arr}')
print(f'original copy: {arr_copy}')