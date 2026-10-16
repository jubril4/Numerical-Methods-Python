#Jubril Hall-Robinson
#October 30, 2023
#Dr.Issa 
#Math355-X01

import numpy as np

# Define the function f(x)
def f(x):
    return np.sin(2*x) - x**3

# Define the derivative of f(x)
def df(x):
    return 2*np.cos(2*x) - 3*x**2

# Fixed iteration method
def fixed_iteration(x0, max_iterations=100, tolerance=1e-4):
    x = x0
    for i in range(max_iterations):
        x_new = x + 0.1 * f(x)  # You can adjust the step size (0.1) as needed
        if abs(x_new - x) < tolerance:
            return x_new
        x = x_new
    return x

# Newton's method
def newton_method(x0, max_iterations=100, tolerance=1e-4):
    x = x0
    for i in range(max_iterations):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tolerance:
            return x_new
        x = x_new
    return x

# Secant method
def secant_method(x0, x1, max_iterations=100, tolerance=1e-4):
    x_prev = x0
    x = x1
    for i in range(max_iterations):
        x_new = x - f(x) * (x - x_prev) / (f(x) - f(x_prev))
        if abs(x_new - x) < tolerance:
            return x_new
        x_prev = x
        x = x_new
    return x

# Initial guesses
x0 = 1.5
x1 = 1.0

# Perform the computations
fixed_result = fixed_iteration(x0)
newton_result = newton_method(x0)
secant_result = secant_method(x0, x1)

# Display the results
print(f"Fixed Iteration Method: x = {fixed_result:.4f}")
print(f"Newton's Method: x = {newton_result:.4f}")
print(f"Secant Method: x = {secant_result:.4f}")
