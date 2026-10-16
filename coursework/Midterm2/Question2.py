#Jubril Hall-Robinson
#October 30, 2023
#Dr.Issa 
#Math355-X01


def false_position_method(func, a, b, tol=1e-6, max_iter=100):
    """
    False Position Method for root finding.

    Parameters:
        func: The function for which to find the root.
        a, b: Initial bracketing interval [a, b].
        tol: Tolerance (stop when |f(x)| < tol).
        max_iter: Maximum number of iterations.

    Returns:
        root: Approximation of the root.
        iterations: Number of iterations performed.
    """
    fa = func(a)
    fb = func(b)

    if fa * fb > 0:
        raise ValueError("Initial interval does not bracket the root.")

    root = None
    iterations = 0

    while iterations < max_iter:
        c = b - (fb * (b - a)) / (fb - fa)
        fc = func(c)

        if abs(fc) < tol:
            root = c
            break

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        iterations += 1

    return root, iterations

# Define the equation
def equation(x):
    return x**(1/3) - 90**(1/3)

# Initial bracketing interval [a, b]
a = 0
b = 100

# Call the false_position_method function
root, iterations = false_position_method(equation, a, b)

# Print the result
print(f"Root: {root}")
print(f"Iterations: {iterations}")