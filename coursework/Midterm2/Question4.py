#Jubril Hall-Robinson
#October 30, 2023
#Dr.Issa 
#Math355-X01


import numpy as np

# Define the function f(x)
def f(x):
    return 2 * np.sin(3 * x)

# Define the point at which we want to approximate the derivative
x = 0.4

# Define step sizes
h_central = 0.05
h_backward = 0.1

# First central difference approximation
central_difference = (f(x + h_central) - f(x - h_central)) / (2 * h_central)

# First noncentral backward difference approximation
noncentral_backward = (3 * f(x) - 4 * f(x - h_backward) + f(x - 2 * h_backward)) / (2 * h_backward)

# Print the results
print("First Central Difference Approximation:", central_difference)
print("First Noncentral Backward Difference Approximation:", noncentral_backward)


