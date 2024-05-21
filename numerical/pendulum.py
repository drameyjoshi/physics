import numpy as np
import matplotlib.pyplot as plt
import scipy

from typing import List

g = 980 # cm/s^2
l = 30  # cm

def derivative_theta(theta_v: np.array, t: float) -> np.array:
    theta, theta_dot = theta_v
    return [theta_dot, -g/l * theta]

def show_motion(t: np.ndarray, thetas: np.ndarray) -> None:
    plt.plot(t, thetas[:, 1], 'g', label=r'$\dot{\theta}(t)$')
    plt.plot(t, thetas[:, 0], 'b', label=r'$\theta(t)$')
    plt.xlabel(r'$t$')
    plt.legend(loc='best')
    plt.title('Motion of a pendulum')
    plt.show()
    
def show_phase_plot(X: np.ndarray,
                    Y: np.ndarray,
                    dX: np.ndarray,
                    dY: np.ndarray) -> None:
    plt.streamplot(X, Y, dX, dY, density=1.6, linewidth=0.5, color='r')
    plt.xlabel(r'$\theta$')
    plt.ylabel(r'$\dot{\theta}$')
    plt.title('Phase portrait of a pendulum')
    plt.show()

def main():
    t = np.linspace(0, 3, 1000)
    theta_0 = [np.pi/180 * 15, 0]
    thetas = scipy.integrate.odeint(derivative_theta, theta_0, t)
    max_theta_dot = np.max(thetas[:, 1])

    Theta = np.arange(-3*np.pi, 3*np.pi, 0.1)
    Theta_dot = np.arange(-10 * max_theta_dot, 10 * max_theta_dot, 0.1)

    T, Td = np.meshgrid(Theta, Theta_dot)
    Tdot = Td
    Tddot = -g/l * np.sin(T)

    show_motion(t, thetas)
    show_phase_plot(T, Td, Tdot, Tddot)
    
if __name__ == '__main__':
    main()
