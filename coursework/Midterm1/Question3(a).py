#Jubril Hall-Robinson
#October 5, 2023 
#Math 355-X01
#Dr.Issa

import numpy as np

#Define x and y data points
x_data = np.array([-1.2, 0.3, 1.1])
y_data = np.array([-5.76, -5.16, -3.69])

#Implement Neville's method 
def neville(x, x_data, y_data):
    n = len(x_data)
    Q = np.zeros((n, n))
    Q[:, 0] = y_data

    for i in range(1, n):
        for j in range(1, i + 1):
            Q[i, j] = ((x - x_data[i - j]) * Q[i, j - 1] - (x - x_data[i]) * Q[i - 1, j - 1]) / (x_data[i] - x_data[i - j])

    return Q[-1, -1]

#Interpolate x
x_interpolated = 0  

#Calculate y at x using Neville's Method 
y_neville = neville(x_interpolated, x_data, y_data)

#Print the solution
print(f"Neville's Method: y at x = {x_interpolated} is approximately {y_neville:.4f}")