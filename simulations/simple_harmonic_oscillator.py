# Simulation of a simple harmonic oscillator
import numpy as np
import scipy
import matplotlib.pyplot as plt

# Physical parameters
omega_sq = 1
init_vals = [2, 0] 

# Algorithmic parameters
start_time = 0
end_time = 15
n_steps = 100
t = np.linspace(start_time, end_time, n_steps)

def shm(t, q):
    return [q[1], -omega_sq * q[0]]

result = scipy.integrate.solve_ivp(fun=shm,
                                t_span=[0,1000],
                                y0=init_vals,
                                t_eval = t)

plt.plot(t, result.y[0])
plt.ylabel(r'$x(t)$')
plt.xlabel(r'$t$')
plt.title('Simple harmonic oscillator')
plt.show()
