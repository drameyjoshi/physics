import numpy as np
import matplotlib.pyplot as plt

# Two constants of the problem.
phi_0 = 1
k = 1

x, z = np.meshgrid(np.linspace(-5, 5), np.linspace(0, 5))
E_x = k*phi_0*np.exp(-k*z) * np.sin(k*x)
E_z = k*phi_0*np.exp(-k*z) * np.cos(k*x)


plt.quiver(x, z, E_x, E_z, color='b')
plt.xlabel('x')
plt.ylabel('z')
plt.title('Electric field in upper half space.')
plt.grid()
plt.savefig('course/purcell_c2p31a.png')
