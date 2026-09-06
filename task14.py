import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x_data =np.array([1,2,3,4,5,6])
y_data =np.array([6,17,34,57,86,121])

def poly2(x,a,b,c):
    return a*x**2 + b*x +c
    
params, covariance = curve_fit(poly2,x_data,y_data)
a,b,c = params

print(f"Fitted polynomial Equation:y={a:.4f}x^2 + {b:.4f}x + {c:.4f}")

x_dense =np.linspace(1,6,200)
y_dense= poly2(x_dense,a,b,c)

plt.figure(figsize=(7,5))
plt.scatter(x_data,y_data, color='red', label='original data points',zorder=5)
plt.plot(x_dense,y_dense, color='blue', label=f'Fitted Curve:{a:.2f}$x^2$ + {b:.2f}$x$ + {c:.2f}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('second - degree polynomial curve fitting using scipy')
plt.legend()
plt.grid(True)
plt.show()



