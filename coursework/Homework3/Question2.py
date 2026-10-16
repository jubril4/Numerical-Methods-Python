#Jubril Hall-Robinson
#September 18, 2023 
#Math 355-X01
#Dr.Issa

#Importing numpy package
import numpy as np

# Define matrix A and vector b
A = np.array([[2, -3, -1],
              [3, 2, -5],
              [2, 4, -1]])

b = np.array([3, -9, -5])

# Augment matrix A with vector b
augmented_matrix = np.column_stack((A, b))

# Perform Gaussian elimination
n = len(augmented_matrix)
x = np.zeros(n)

# Forward elimination
for i in range(n):
    # Make the diagonal element 1
    diagonal_element = augmented_matrix[i][i]
    augmented_matrix = augmented_matrix[i]/diagonal_element

    # Eliminate non-zero elements below the diagonal
    for i in range(i + 1, n):
        factor = augmented_matrix[i]
        augmented_matrix[i] -= factor * augmented_matrix[i]

# Back-substitution
x[n - 1] = augmented_matrix[n - 1][-1]
for i in range(n - 2, -1, -1):
    x[i] = augmented_matrix[i][-1] - np.dot(augmented_matrix[i][i + 1:n - 1], x[i + 1:])

# Print the solution
print("Solution vector x:")
print(x)
