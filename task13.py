import numpy as np
from scipy.integrate import quad

def f(x):
	return x**2 + 2*x +1
	
def numerical_derivative(func,x,h=1e-5):
	return (func(x+h)- func(x-h))/ (2*h)
	
x_point = 3.0
a,b=0.0,2.0

diff_val= numerical_derivative(f,x_point)
print(f"Derivative of f(x) at x={x_point}:{diff_val:.4f}")

integral_val,error=quad(f,a,b)
print(f"Definite integralof f(x) from {a} to  {b}:{integral_val:.4f}(EstimateError: {error:.2e})")

