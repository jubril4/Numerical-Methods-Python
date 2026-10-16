#Jubril Hall-Robinson
#September 18, 2023 
#Math 355-X01
#Dr.Issa

#Importing numpy package
import numpy as np

# Define the coefficient matrix A
A = np.array([
    [0, 2, 5, -1],
    [2, 1, 3, 0],
    [-2, -1, 3, 1],
    [3, 3, -1, 2]
])

# Define the right-hand side vector B
B = np.array([-3, 3, -2, 5])

# Solve for the variables X
X = np.linalg.solve(A, B)

# The solution for X will be stored in the X array
print("Solution:")
print(X)
