import numpy as np
from scipy.optimize import minimize

"""def objective_function(vars):
    x,y=vars
    return (x-2)**2 + (y-2)**2"""
def objective_function1(vars):
    x,y=vars
    return np.sin(x)+ np.cos(y)
    
initial_guess =[0.0,0.0]
    
#result = minimize(objective_function, initial_guess, method='BFGS')
result = minimize(objective_function1, initial_guess, method='BFGS')   
print(f"Optimization success: {result.success}")
print(f"Optimal point (x,y): ({result.x[0]:.4f},{result.x[1]:.4f})")
print(f"Minimum Function Value: {result.fun:.6e}")
