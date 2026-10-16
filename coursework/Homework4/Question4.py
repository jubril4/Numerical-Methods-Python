#Jubril Hall-Robinson
#September 28, 2023 
#Math 355-X01
#Dr.Issa


#import numpy to implement arrays

import numpy as np

#Function definition

def func_Neville(x_Arr, y_Arr, x_int):
    

#Get the size

    n = x_Arr.size

#Insert y value in the first column of q matrix

q_Matrix = np.zeros((n, n - 1))

q_Matrix = np.concatenate((y_Arr[:, None], q_Matrix), axis=1)

#Loop through the size

for i in range(1, n):

#Loop through i+1

    for j in range(1, i + 1):

#Calculate y values and store the result in the matrix

        q_Matrix[i, j] = ((x_int - x_Arr[i - j]) * q_Matrix[i, j - 1] -

(x_int - x_Arr[i]) * q_Matrix[i - 1, j - 1]) / (x_Arr[i] - x_Arr[i - j])

#Store the interpolated values

y_int = q_Matrix[n - 1, n - 1]

#Return interpolated value

return y_int

#Assign value of pi

pi = 3.14

#Store the values of x and y in the respective arrays

x_Arr = np.array([0, 0.5, 1, 1.5, 2])

y_Arr = np.array([-1.0, 1.75, 4.00, 5.75, 7.00])

#Call the function by passing x value

print("Y at x= pi/4 is: ",func_Neville(x_Arr, y_Arr, pi/4))