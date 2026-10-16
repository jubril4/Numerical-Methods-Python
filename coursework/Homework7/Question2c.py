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

# Number of sub-intervals (should be a multiple of 3)
n = 6

# Calculate the step size
h = (b - a) / n

# Calculate the Simpson 3/8 integration
integral = f(a) + f(b)

for i in range(1, n, 3):
    integral += 3 * (f(a + i * h) + f(a + (i + 1) * h))

for i in range(3, n-1, 3):
    integral += 2 * f(a + i * h)

integral *= 3 * h / 8

print("Simpson 3/8 Integration Result:", integral)
