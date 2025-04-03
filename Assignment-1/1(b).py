import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 400)
y = np.linspace(-1, 1, 400)
X, Y = np.meshgrid(x, y)

Z = (X**2 + Y**2)**2 - 2 * Y * X**2

plt.contour(X, Y, Z, levels=[0], colors='green')

plt.xlabel("x")
plt.ylabel("y")
plt.title(r"Plot of $(x^2 + y^2)^2 = 2yx^2$")
plt.grid(True)
plt.axhline(0, color='b')
plt.axvline(0, color='b')
plt.axis("equal")
plt.show()
