#Jubril Hall-Robinson
#September 18, 2023 
#Math 355-X01
#Dr.Issa

#Importing numpy package
import numpy as np

# Define the matrix
matrix = np.array([[9, 1, 3],
                   [-2, -3, 4],
                   [3, 11, 7]])

# Calculate the determinant of the matrix
det = np.linalg.det(matrix)

# Check if the determinant is zero
if det == 0:
    print("The matrix is singular, and its inverse does not exist.")
else:
    # Calculate the inverse using numpy's linalg.inv function
    inverse_matrix = np.linalg.inv(matrix)

    print("Inverse of the matrix:")
    print(inverse_matrix)
