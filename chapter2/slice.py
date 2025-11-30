# slicing numpy array
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[1:5]) #[2 3 4 5]
print(arr[3:]) #[4 5 6 7 8 9]
print(arr[:5]) #[1 2 3 4 5]
print(arr[-3:]) #[7 8 9]
print(arr[:-3]) #[1 2 3 4 5 6]
print(arr[1:5:2]) #[2 4]
print(arr[::2]) #[1 3 5 7 9]

# slicing 2D numpy array
np2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np2[1:]) #[[4 5 6]
               # [7 8 9]]
print(np2[1,2]) #6, from 1st item and 2nd element
print(np2[1,1:]) #[5 6]
print(np2[1:,1:]) #[[5 6]
                  # [8 9]]
print(np2[0:1, 1:2]) #[[2]]
print(np2[0:2, 1:3]) #[[2 3]
                        # [5 6]]
