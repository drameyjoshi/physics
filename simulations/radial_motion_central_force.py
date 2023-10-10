import numpy as np
import scipy
import matplotlib.pyplot as plt

# Physical parameters
k = 1 # The 'constant' of the force.
m = 1 # Mass of the particle.

# Constants of motion.
angular_momentum = 0.8

def V_eff(r: float,
          L: float,
          k: float,
          m: float) -> float:
    """
    Effective potential energy as a function of r.

    Parameters:
    r is the radial distance.
    L is the angular momentum.
    k is the 'constant' of the force.
    m is the mass of the particle.
    """
    return -k/r + L**2/(2 * m * r**3)

def law(t: float, y: np.array) -> np.array:
    """
    The 'law of motion'. It is the RHS of the equation of motion in matrix
    form. The arguments are as required by `scipy.integrate.solve_ivp`.
    """
    return [y[1], -k/y[0]**2 + angular_momentum**2/(m**2 * y[0]**3)]

show_V_eff = True
if show_V_eff:
    R = np.linspace(0.5, 5, 100)
    plt.plot(R, V_eff(R, angular_momentum, k, m))
    plt.xlabel(r'$r$')
    plt.ylabel(r'$V_\text{eff}(r)$')
    plt.title('Effective potential energy of 1-d motion.')
    plt.show()

# The initial position was chosen after consulting the plot of effective
# potential energy. I am interested in bounded motion.
init_r = 0.75
init_y = [init_r, angular_momentum * init_r/m]
init_E = -k * m/init_y[0] + m * init_y[1]**2/2
print(f'Energy = {init_E}')

# Algorithm settings.
time_span = [0, 14]
t_eval = np.linspace(time_span[0], time_span[1], num=100)

solution = scipy.integrate.solve_ivp(fun=law,
                                     t_span=time_span,
                                     y0=init_y,
                                     t_eval=t_eval)
plt.plot(solution.t, solution.y[0])
plt.xlabel(r'$t$')
plt.xlabel(r'$r(t)$')
plt.title('Radial motion')
plt.show()
