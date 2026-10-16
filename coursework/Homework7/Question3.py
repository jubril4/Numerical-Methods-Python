#Jubril Hall-Robinson
#November 4, 2023 
#Math 355-X01
#Dr.Issa




import numpy as np

# Define the function to be integrated
def f(x):
    return x**2

# Number of iterations (k=3)
k = 3

# Create a table for Romberg integration
R = np.zeros((k, k))

# Step 1: Calculate the first column (i=0) using the trapezoidal rule
a = 0  # Lower limit
b = 1  # Upper limit
h = b - a  # Initial step size

R[0, 0] = (f(a) + f(b)) * h / 2

# Step 2: Fill in the rest of the table using Richardson extrapolation
for i in range(1, k):
    h /= 2  # Halve the step size
    total = 0
    for j in range(1, 2**i, 2):
        total += f(a + j * h)
    R[i, 0] = R[i - 1, 0] / 2 + h * total

    # Calculate the remaining columns using extrapolation
    for j in range(1, i + 1):
        R[i, j] = R[i, j - 1] + (R[i, j - 1] - R[i - 1, j - 1]) / ((4**j) - 1)

# The value of R(3, 3) is the final entry in the table
result = R[k - 1, k - 1]

print(f"R(3, 3) = {result:.6f}")
