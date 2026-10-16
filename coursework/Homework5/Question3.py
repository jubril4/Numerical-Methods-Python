#Jubril Hall-Robinson
#October 20, 2023 
#Math 355-X01
#Dr.Issa

import sympy as sp

# Define the symbols and the polynomials
x = sp.symbols('x')

P4 = x**4 + 2.1*x**3 - 2.52*x**2 + 2.1*x - 3.52
P5 = x**5 - 156*x**4 - 5*x**3 + 780*x**2 + 4*x - 624
P6 = x**6 + 4*x**5 - 8*x**4 - 34*x**3 + 57*x**2 + 130*x - 150

# Find the roots
roots_P4 = sp.solve(P4, x)
roots_P5 = sp.solve(P5, x)
roots_P6 = sp.solve(P6, x)

print("Roots of P4(x):", roots_P4)
print("Roots of P5(x):", roots_P5)
print("Roots of P6(x):", roots_P6)