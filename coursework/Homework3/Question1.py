#Jubril Hall-Robinson
#September 20p, 2023 
#Math 355-X01
#Dr.Issa

#Importing numpy package
import numpy as np

# Define the LU decomposition matrices L and U
L = np.array([[1, 0, 0],
              [3/2, 1, 0],
              [1/2, 11/13, 1]])

U = np.array([[2, -3, -1],
              [0, 13/2, -7/2],
              [0, 0, 32/13]])

# Define the right-hand side vector b
b = np.array([1, -1, 2])

# Solve Ly = b for y using forward substitution
y = np.linalg.solve(L, b)

# Solve Ux = y for x using backward substitution
x = np.linalg.solve(U, y)

print("Solution x:", x)
