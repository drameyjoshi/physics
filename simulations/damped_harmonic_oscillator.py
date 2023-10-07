# Simulation of a damped harmonic oscillator
import numpy as np
import scipy
import matplotlib.pyplot as plt

# Physical parameters
omega_sq = 1 # Angular frequency squared
gamma = -0.1  # Damping constant
init_vals = [2, 0] # Initial position, initial velocity

# Algorithmic parameters
start_time = 0
end_time = 50
n_steps = 1000
t = np.linspace(start_time, end_time, n_steps)

def dhm(t, q):
    return [q[1], -omega_sq * q[0] + gamma * q[1]]

result = scipy.integrate.solve_ivp(fun=dhm,
                                t_span=[0,1000],
                                y0=init_vals,
                                t_eval = t)

plt.plot(t, result.y[0])
plt.ylabel(r'$x(t)$')
plt.xlabel(r'$t$')
plt.title('Damped harmonic oscillator')
plt.show()
