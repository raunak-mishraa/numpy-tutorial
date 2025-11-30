# universal functions
import numpy as np
arr = np.array([-3,-2,-1,0,1, 2, 3, 4, 5, 6, 7, 8, 9])

# square root of each element
print(np.sqrt(arr))

# absolute value 
print(np.absolute(arr)) # [3 2 1 0 1 2 3 4 5 6 7 8 9]

#exponents, e^x , where x is each element, e=2.71828
print(np.exp(arr)) # [4.97870684e-02 1.35335283e-01 3.67879441e-01 1.00000000e+00 2.71828183e+00 7.38905610e+00 2.00855369e+01 5.45981500e+01 1.48413159e+02 4.03428793e+02 1.09663316e+03 2.98095799e+03 8.10308393e+03]

# Minimum and Maximum
print(np.min(arr)) # -3
print(np.max(arr)) # 9

# sign positive or negative
print(np.sign(arr)) # [-1 -1 -1  0  1  1  1  1  1  1  1  1  1]

#trig
print(np.sin(arr)) # [-0.14112001 -0.90929743 -0.84147098  0.          0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427 -0.2794155   0.6569866   0.98935825  0.41211849]

#log
print(np.log(arr)) # [       nan        nan        nan       -inf 0.         0.69314718 1.09861229 1.38629436 1.60943791 1.79175947 1.94591015 2.07944154 2.19722458]