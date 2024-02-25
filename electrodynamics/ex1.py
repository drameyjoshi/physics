import matplotlib.pyplot as plt
import numpy as np


t = np.linspace(start = 0, stop = 10)
v = [11] * len(t)
x = v * t

v1 = 1.1 * t
x1 = v1 * t

v2 = 20 - t
x2 = v2 * t

x3 = [10] * len(t)

plt.plot(x, t, label='Uniform speed', color='green')
plt.plot(x1, t, label='Acceleration', color='blue')
plt.plot(x2, t, label='Deceleration', color='orange')
plt.plot(x3, t, label='Stationary', color='red')
plt.xlabel(r'$x$')
plt.ylabel(r'$t$')
plt.title(r'World lines of particles moving along $x$-axis')
plt.legend()
plt.savefig('ex1.png')
plt.show()

