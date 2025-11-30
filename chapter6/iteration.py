import numpy as np

#1d array
arr = np.array([1, 2, 3, 4, 5 ,6, 7, 8, 9, 10])
for x in arr:
    print(x)

#2d array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr2d:
    # print rows
    print(x)

# print each element
for x in arr2d:
    for y in x:
        print(y)

#3d array
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# for x in arr3d:
#     # print 2d array
#     print(x)

# print each element
# for x in arr3d:
#     for y in x:
#         for z in y:
#             print(z)

#let's get into an easy way, using nditer
for x in np.nditer(arr3d):
    print(x)