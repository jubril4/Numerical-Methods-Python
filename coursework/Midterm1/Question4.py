#Jubril Hall-Robinson
#October 5, 2023 
#Math 355-X01
#Dr.Issa

import numpy as np
from scipy.interpolate import CubicSpline

# Define the data points
x = np.array([0, 1, 2])
y = np.array([0, 2, 1])

# Create a cubic spline interpolation for the given data
spline = CubicSpline(x, y, bc_type='natural')

# Evaluate the spline at x = 1 and x = 2
spline_at_1 = spline(1)
spline_at_2 = spline(2)

print("Spline at x=1:", spline_at_1)
print("Spline at x=2:", spline_at_2)

# Verify that the cubics have the same first and second derivatives at x = 1
spline_derivative_1 = spline.derivative()(1)
spline_derivative_2 = spline.derivative()(2)

#Print the solution
print("First derivative at x=1:", spline_derivative_1)
print("First derivative at x=2:", spline_derivative_2)