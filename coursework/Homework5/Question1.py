#Jubril Hall-Robinson
#October 20, 2023 
#Math 355-X01
#Dr.Issa

import math

# Define the function f(x)
def f(x):
    return math.sin(x) + 3 * math.cos(x) - 2

# Define the derivative of the function f(x)
def df(x):
    return math.cos(x) - 3 * math.sin(x)

# Initial guess for the root
x0 = 1.0

# Tolerance for stopping the iteration
tolerance = 1e-6

# Maximum number of iterations
max_iterations = 100

# Newton-Raphson method
for i in range(max_iterations):
    x1 = x0 - f(x0) / df(x0)
    if abs(x1 - x0) < tolerance:
        break
    x0 = x1

print("Root:", x0)