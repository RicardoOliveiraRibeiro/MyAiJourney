# Example Python script for computing derivatives
import sympy as sp

# Define a symbolic variable and function
x = sp.Symbol('x')
f = x**2 + 3*x + 2

# Compute the derivative of the function
f_prime = sp.diff(f, x)
print("Derivative of the function:")
print(f_prime)
