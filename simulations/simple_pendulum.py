# Simulation of a simple pendulum
import numpy as np
import scipy
import matplotlib.pyplot as plt

# Physical parameters
l = 10 # Length of the pendulum
init_vals = [np.pi/2, 0] # Initial angular position, initial angular velocity

# Equation of motion
def sp(t, q):
    return [q[1], -scipy.constants.g * np.sin(q[0])/l]


# Algorithmic parameters
grid_size = 20
max_omega = 3.0
all_thetas = np.linspace(-np.pi, np.pi, grid_size)
all_omegas = np.linspace(-max_omega, max_omega, grid_size)

Thetas, Omegas = np.meshgrid(all_thetas, all_omegas)

next_thetas = np.zeros(Thetas.shape)
next_omegas = np.zeros(Omegas.shape)

nrows, ncols = next_thetas.shape
t = 0
for i in range(nrows):
    for j in range(ncols):
        theta = Thetas[i, j]
        omega = Omegas[i, j]
        result = sp(t, [theta, omega])
        next_thetas[i, j] = result[0]
        next_omegas[i, j] = result[1]

plt.quiver(Thetas, Omegas, next_thetas, next_omegas, color='b')
plt.xlabel(r'$\theta$')
plt.ylabel(r'$\omega$')
plt.xlim([-np.pi, np.pi])
plt.ylim([-max_omega - 1, max_omega + 1])
plt.title('Phase portrait of a simple pendulum')
plt.show()


