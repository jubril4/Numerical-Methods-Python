import numpy as np

# Define the matrices L and U
L = np.array([[1, 0, 0],
              [3/2, 1, 0],
              [1/2, 11/13, 1]])

U = np.array([[2, -3, -1],
              [0, 13/2, -7/2],
              [0, 0, 32/13]])

# Define the vector b
b = np.array([1, -1, 2])

# Solve Ly = b for y using forward substitution
y = np.linalg.solve(L, b)

# Solve Ux = y for x using back substitution
x = np.linalg.solve(U, y)

# Print the solution vector x
print("Solution x:")
print(x)
