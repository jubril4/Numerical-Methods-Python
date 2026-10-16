#Jubril Hall-Robinson
#October 5, 2023 
#Math 355-X01
#Dr.Issa




import numpy as np

#Define x and y data points
x_data = np.array([-1.2, 0.3, 1.1])
y_data = np.array([-5.76, -5.16, -3.69])

#Implement Lagrange's Method 
def lagrange(x, x_data, y_data):
    n = len(x_data)
    result = 0

    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if j != i:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        result += term

    return result

 #Interpolate X
x_interpolated = 0 

#Calculate y at x using Lagrange's Method 
y_lagrange = lagrange(x_interpolated, x_data, y_data)

#Print the solution
print(f"Lagrange's Method: y at x = {x_interpolated} is approximately {y_lagrange:.4f}")


