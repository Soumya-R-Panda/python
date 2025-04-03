import numpy as np
import matplotlib.pyplot as plt
from mandelbrot import mandelbrot_set

def plot_mandelbrot(filename="mandelbrot.npy", xmin = -2 , xmax = 2 , ymin = -2 , ymax = 2 ):
    x = np.load(filename)
    plt.imshow(x, extent=( xmin, xmax, ymin, ymax), cmap='inferno', origin='lower')
    plt.colorbar()
    plt.title("Mandelbrot Set")
    plt.show()


plot_mandelbrot()

def zoomed_mandelbrot(xmin, xmax, ymin, ymax, step):
    zoom_data = mandelbrot_set(xmin, xmax, ymin, ymax, step)
    np.save("mandelbrot_zoom.npy", zoom_data)
    plot_mandelbrot("mandelbrot_zoom.npy", xmin, xmax, ymin, ymax)

zoomed_mandelbrot(0.25, 0.3, 0, 0.02, 0.0002)
