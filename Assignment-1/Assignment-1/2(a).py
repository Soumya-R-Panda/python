import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 500) 
r = 3 * theta

plt.subplot(111, projection='polar')
#yahan se ekbar projection hatake dekho
plt.plot(theta, r, color='green')
plt.grid(True)

plt.show()
