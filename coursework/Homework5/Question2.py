#Jubril Hall-Robinson
#October 20, 2023 
#Math 355-X01
#Dr.Issa


import sympy as sp

# Define the symbolic variable x
x = sp.symbols('x')

# Define the polynomial equation
equation = x**4 + 0.9*x**3 - 2.3*x**2 + 3.6*x - 25.2

# Find the derivative of the equation
derivative = sp.diff(equation, x)

# Define the initial guess
initial_guess = 2.0

# Set a tolerance level for convergence
tolerance = 1e-6

# Maximum number of iterations
max_iterations = 100

# Initialize the Newton-Raphson loop
x_n = initial_guess
for i in range(max_iterations):
    f_x_n = equation.subs(x, x_n)
    f_prime_x_n = derivative.subs(x, x_n)
    
    if abs(f_x_n) < tolerance:
        break

    x_n = x_n - f_x_n / f_prime_x_n

print(f"Approximate root: {x_n}")