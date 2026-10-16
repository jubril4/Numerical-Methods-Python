


from scipy.optimize import newton

# Define the function
def f(x):
    return x**3 + 12*x**2 - 100*x - 6

def df(x):
        return 3*x**2 + 24*x - 100

# Initial guesses
x0_a = -8
x0_b = 8

# Use Newton-Raphson to estimate the roots
root_a = newton(f, x0_a, fprime=df)
root_b = newton(f, x0_b, fprime=df)

root_a, root_b

