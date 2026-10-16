#Jubril Hall-Robinson
#October 5, 2023 
#Math 355-X01
#Dr.Issa

import numpy as np

# Define coefficient matrix A
A = np.array([[0, 2, 5, -1],
              [2, 1, 3, 0],
              [-2, -1, 3, 1],
              [3, 3, -1, 2]])

# Define right side vector b
b = np.array([-3, 3, -2, 5])

# Solve for x using the numpy.linalg.solve function
x = np.linalg.solve(A, b)

# Print solution
print("Solution:")
print("x1 =", x[0])
print("x2 =", x[1])
print("x3 =", x[2])
print("x4 =", x[3])