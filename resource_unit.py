#import numpy
import numpy as np

#create the resource consumption matrix
mat = np.array([[2, 1], [1, 3]])

#create the inverse of the resource consumption matrix
mat_inv = np.linalg.inv(mat)

#create a 2 by 1 available resource matrix
a = np.array([[8], [11]])

#find the units needed

units = mat_inv @ a
print("UNITS AVAILABLE: ", units)



