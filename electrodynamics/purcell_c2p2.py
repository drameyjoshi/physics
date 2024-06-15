import numpy as np
import matplotlib.pyplot as plt

def varphi(z: float) -> float:
    return 12/z - 6/(z - 3)
    
Z1 = np.linspace(-6, 6)
Z2 = np.linspace(-0.1, 0.1)
Z3 = np.linspace(2.9, 3.1)

Z = np.concatenate((Z1, Z2, Z3))
Z.sort()
V = [varphi(z) for z in Z]

plt.plot(Z, V)
plt.xlabel(r'$z$')
plt.ylabel(r'$\varphi(0, 0, z)$')
plt.title('Potential due to two charges on the z-axis')
plt.show()
