#Jubril Hall-Robinson
#October 30, 2023
#Dr.Issa 
#Math355-X01

#Bisection method is advantageous when:

#1. A continuous function with known initial bounds (a and b) where the root exists.

#2. Function is not differentiable, or finding the derivative is challenging.

#3.To ensure convergence to a solution even when the function is not well-behaved or has multiple roots.

#Define function of the equation
def f(x):
    return 2*x**2 - 4*x - 10

#Perform bisection method
def bisection(a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        print("Bisection method may not converge.")
        return None

    for i in range(max_iter):
        c = (a + b) / 2
        if f(c) == 0 or (b - a) / 2 < tol:
            return c
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2

a = 0
b = 5
tolerance = 1e-5
max_iterations = 4

#Result of the function
result = bisection(a, b, tolerance, max_iterations)

if result:
    print(f"Positive root found using bisection method: {result:.5f}")
else:
    print("Bisection method did not converge.")

  
 # Newton-Raphson method is advantageous when:


#1. The function is differentiable.

#2. We want faster convergence, especially for well-behaved functions.


#Define Function Equation

def f(x):
    return 2*x**2 - 4*x - 10

def df(x):
    return 4*x - 4

#Perform Newton Raphson

def newton_raphson(x0, tol, max_iter):
    for i in range(max_iter):
        if df(x0) == 0:
            print("Derivative is zero. Newton-Raphson may not converge.")
            return None

        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1

    return None

initial_guess = 3
tolerance = 1e-5
max_iterations = 4

result = newton_raphson(initial_guess, tolerance, max_iterations)

#Result of the equation
if result:
    print(f"Positive root found using Newton-Raphson method: {result:.5f}")
else:
    print("Newton-Raphson method did not converge.")

  