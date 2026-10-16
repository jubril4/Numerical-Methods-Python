#Jubril Hall-Robinson
#September 28, 2023 
#Math 355-X01
#Dr.Issa


import numpy as np
import scipy
from scipy.optimize import curve_fit

# Define the function f(x) = ax^b
def func(x, a, b):
    return a * x**b

# Define the data
x_data = np.array([0.5, 1.0, 1.5, 2.0, 2.5])
y_data = np.array([0.49, 1.60, 3.36, 6.44, 10.16])

# Use curve_fit to fit the function to the data
params, covariance = curve_fit(func, x_data, y_data)

# Extract the values of a and b
a, b = params

print(f'a = {a}, b = {b}')