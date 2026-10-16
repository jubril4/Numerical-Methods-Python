#Jubril Hall-Robinson
#October 5, 2023 
#Math 355-X01
#Dr.Issa

import numpy as np
from scipy.optimize import curve_fit

# Define the data points
T = np.array([79, 190, 357, 524, 690])
k = np.array([1.00, 0.932, 0.839, 0.759, 0.693])

# Define the quadratic function to fit
def quadratic_fit(x, a, b, c):
    return a * x**2 + b * x + c

# Fit the data to the quadratic function using curve_fit
params, covariance = curve_fit(quadratic_fit, T, k)

# Extract the coefficients (a, b, c) from the fitted parameters
a, b, c = params

# Calculate the fitted values using the quadratic function
k_fit = quadratic_fit(T, a, b, c)
#Print the solution
print("Fitted Quadratic Coefficients (a, b, c):", a, b, c)


