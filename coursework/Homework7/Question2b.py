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

# Number of sub-intervals (should be even)
n = 4

# Calculate the step size
h = (b - a) / n

# Calculate the Simpson 1/3 integration
integral = f(a) + f(b)

for i in range(1, n, 2):
    integral += 4 * f(a + i * h)

for i in range(2, n-1, 2):
    integral += 2 * f(a + i * h)

integral *= h / 3

print("Simpson 1/3 Integration Result:", integral)
