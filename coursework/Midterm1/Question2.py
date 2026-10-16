#Jubril Hall-Robinson
#October 5, 2023 
#Math 355-X01
#Dr.Issa

import numpy as np

# Define coefficient matrix A and right side vector b
A = np.array([[12, -2, 3, 1],
              [-2, 15, 6, -3],
              [1, 6, 20, -4],
              [0, -3, 2, 9]], dtype=float)  # dtype float allows decimal division

b = np.array([0, 0, 20, 0], dtype=float)

# Augment coefficient matrix with the right-hand side vector
augmented_matrix = np.column_stack((A, b))

# Perform Gaussian elimination
n = len(b)

for i in range(n):
    # Partial pivoting
    max_row = i
    for j in range(i + 1, n):
        if abs(augmented_matrix[j, i]) > abs(augmented_matrix[max_row, i]):
            max_row = j
    augmented_matrix[[i, max_row]] = augmented_matrix[[max_row, i]]
    
    # Elimination
    for j in range(i + 1, n):
        factor = augmented_matrix[j, i] / augmented_matrix[i, i]
        augmented_matrix[j, i:] -= factor * augmented_matrix[i, i:]

# Back substitution to find x
x = np.zeros(n)
for i in range(n - 1, -1, -1):
    x[i] = (augmented_matrix[i, -1] - np.dot(augmented_matrix[i, i+1:n], x[i+1:])) / augmented_matrix[i, i]

# Print solution
print("Solution:")
for i in range(n):
    print(f"x{i+1} = {x[i]}")