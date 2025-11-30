import numpy as np
# Create 1-D array and Get the shape
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr.shape) # (9,) 9 elements

# Create a 2-D array and Get the shape (rows, columns)
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d.shape) # (2, 3) 2 rows and 3 columns

#Reshape 1-D to 2-D  
arr3 = arr.reshape(4,3)
print(arr3) # [[ 1  2  3] [ 4  5  6] [ 7  8  9] [10 11 12]]
print(arr3.shape) # (4, 3) 4 rows and 3 columns

#Reshape 3-D
arr4 = arr.reshape(2,3,2) # 2 arrays, 3 rows, 2 columns
print(arr4) # [[[ 1  2] [ 3  4] [ 5  6]] [[ 7  8] [ 9 10] [11 12]]]

#flatten to 1-D
arr5 = arr4.reshape(-1)
print(arr5) # [ 1  2  3  4  5  6  7  8  9 10 11 12]
arr6 = arr4.flatten()
print(arr6) # [ 1  2  3  4  5  6  7  8  9 10 11 12]