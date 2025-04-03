import numpy as np
import matplotlib.pyplot as plt

def mandelbrot_set(xmin=-2, xmax=2, ymin=-2, ymax=2, step=0.01):
    real = np.arange(xmin, xmax + step  , step)
    imag = np.arange(ymin, ymax  + step , step)

    result = np.zeros((len(imag), len(real)))
    
    for i,c_real in enumerate(real):
        for j,c_imag in enumerate(imag):
            c = complex(c_real , c_imag)
            z = complex(0, 0)
            count = 0
            
            while abs(z)<= 2 and count < 2000:
                z = z**2 + c
                count += 1
            
            result[j, i] = count
    
    np.save("mandelbrot.npy", result)
    return result


mandelbrot_set()



