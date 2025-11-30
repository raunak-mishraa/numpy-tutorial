# Numpy - Numerical Python, anything in the numpy array has to be of the same type
# so the datatype of the numpy is ndarray which is n-dimensional array, so list can multi-dimensional array, it not only have array but also have lot of mathematical functions
import numpy as np

# creating a numpy array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) 
print(arr) # [1 2 3 4 5 6 7 8 9]

# gives the shape of the array
#returns a tuple representing the dimensions of the array, A 1D array with 9 elements will have a shape of (9,), A 2D array (matrix) with 3 rows and 3 columns will have a shape of (3, 3).
print(arr.shape) #(9,)

#give the size of the array
print(arr.size) #9

# gives the dimension of the array
print(arr.ndim) #1

# gives the datatype of the array
print(arr.dtype) #int32

#similar to Python's built-in range() function but returns a NumPy array,
np2 = np.arange(10)
print(np2) #[0 1 2 3 4 5 6 7 8 9]

print(np.arange(1, 10, 2)) #[1 3 5 7 9]

# zeros() function returns a new array of given shape and type, filled with zeros.
print(np.zeros((3, 3))) #[[0. 0. 0.]
                        # [0. 0. 0.]
                        # [0. 0. 0.]]
print(np.zeros(5)) #[0. 0. 0. 0. 0.]
# ones() function returns a new array of given shape and type, filled with ones.
print(np.ones((3, 3))) #[[1. 1. 1.]
                        # [1. 1. 1.]
                        # [1. 1. 1.]]
# full() function returns a new array of given shape and type, filled with fill_value.
print(np.full((2, 2), 9)) #[[9 9]
                           # [9 9]]
# Convert a list into a numpy array
list = [1, 2, 3, 4, 5]
arr = np.array(list)
print(arr) #[1 2 3 4 5]
print(arr[0]) #1