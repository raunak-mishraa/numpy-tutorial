import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7,4,8, 9])
x = [True, False, True, False, True, False, True, False, True, False]
print(arr[x]) # [1 3 5 7 9]

filtered = []
for i in arr:
    if i % 2 == 0:
        filtered.append(True)
    else:
        filtered.append(False)
print(arr[filtered]) # [2 4 6 4 8]

# Shorter version
filtered = arr % 2 == 1
print(arr[filtered]) # [1 3 5 7 9]
