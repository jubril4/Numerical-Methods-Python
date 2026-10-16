#Jubril Hall-Robinson
#November 4, 2023 
#Math 355-X01
#Dr.Issa


import numpy as np

# Define the function to be integrated
def f(x):
    return x**2

# Define the integration limits
a = 0
b = 1

# Number of sub-intervals
n = 4

# Calculate the step size
h = (b - a) / n

# Calculate the trapezoidal integration
integral = 0.5 * (f(a) + f(b))

for i in range(1, n):
    integral += f(a + i * h)

integral *= h

print("Trapezoidal Integration Result:", integral)
