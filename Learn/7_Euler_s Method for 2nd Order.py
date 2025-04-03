import numpy as np
import matplotlib.pyplot as plt

def euler_method(omega, x_t0, v_t0, tSTART, tEND, N=1000):
    delt = (tEND - tSTART) / N
    t = np.linspace(tSTART, tEND, N+1)
    x = np.zeros(N+1)
    v = np.zeros(N+1)
    x[0] = x_t0
    v[0] = v_t0

    for i in range(N):
        x[i+1] = x[i] + delt * v[i]
        v[i+1] = v[i] - delt * omega**2 * x[i]

    return t, x, v

omega = 1
x_t0 = 0.5
v_t0 = 0
tSTART = 0
tEND = 10
t, x, v = euler_method(omega, x_t0, v_t0, tSTART, tEND)


m = 1
K = 0.5 * m * v**2
U = 0.5 * m * omega**2 * x**2
E = K + U

plt.plot(t, x , color='green')
plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("Displacement vs Time")
plt.grid()
plt.show()

plt.plot(t, v , color='red')
plt.xlabel("t")
plt.ylabel("v(t)")
plt.title("Velocity vs Time")
plt.grid()
plt.show()

plt.plot(t, E , color='blue')
plt.xlabel("t")
plt.ylabel("Energy")
plt.title("Total Energy vs Time")
plt.grid()
plt.show()
