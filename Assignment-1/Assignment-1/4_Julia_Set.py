import numpy as np
import matplotlib.pyplot as plt

def julia_set(c, xmin=-2, xmax=2, ymin=-2, ymax=2, step=0.01):
    real = np.arange(xmin, xmax, step)
    imag = np.arange(ymin, ymax, step)

    result = np.zeros((len(imag), len(real)))

    for i,z_real in enumerate(real):
        for j,z_imag in enumerate(imag):
            z = complex(z_real, z_imag)
            count = 0

            # Iterate using the formula: z = z**2 + c
            while abs(z) <= 2 and count < 2000:
                z = z**2 + c
                count += 1

            result[j, i] = count

    return result

c = complex(-0.4, 0.6)

data = julia_set(c)

plt.figure(figsize=(20, 20))
plt.imshow(data, extent=(-2, 2, -2, 2), cmap='inferno', origin='lower')
plt.colorbar()
plt.title("Julia Set for -0.4 + 0.6i")
plt.show()
