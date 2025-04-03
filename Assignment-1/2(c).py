import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0 , 2 * np.pi , 1000)
r = np.exp(np.cos(theta)) - 2 * np.cos(4 * theta) + np.sin(theta/12)**4

plt.subplot(111 , projection = 'polar')
plt.plot(theta , r ,color = "Green")
plt.grid(True)
plt.show()
