import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 400)  
y = np.linspace(-2, 2, 400)  
X, Y = np.meshgrid(x, y)  

Z = X**2 + Y**2
plt.contour(X, Y, Z, levels=[2], colors='Green')
plt.axis('equal')
plt.grid(True)
plt.show()
