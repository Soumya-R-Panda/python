import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0 , 4 * np.pi , 500)
r = np.exp(4*theta)

plt.subplot(111 , projection = 'polar')
plt.plot(theta , r , color = 'Green')
plt.grid(True)
plt.show()
