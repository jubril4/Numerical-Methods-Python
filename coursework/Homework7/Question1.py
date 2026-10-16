#Jubril Hall-Robinson
#November 4, 2023 
#Math 355-X01
#Dr.Issa

import numpy as np

# Define the function to be integrated
def f(x):
    return x**2  # Replace this with your desired function

# Define the integration limits
a = 0  # Lower limit
b = 1  # Upper limit

# Number of sub-intervals
n = 4

# Calculate the step size
h = (b - a) / n

# Calculate the trapezoidal integration
integral = 0.5 * (f(a) + f(b))  # Initialize with the first and last values

for i in range(1, n):
    integral += f(a + i * h)

integral *= h

print("Trapezoidal Integration Result:", integral)
