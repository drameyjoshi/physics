import matplotlib.pyplot as plt
import numpy as np

q = 1 # esu
R = 10 # cm

def main() -> None:
    thetas = np.linspace(0, np.pi, 100)
    sinsq = np.sin(thetas)**2
    a = q/R**2

    beta = 0.25
    Es = (q/R**2) * (1 - beta**2)/(1 - beta**2 * np.sin(thetas)**2)**(3/2)
    plt.plot(thetas, Es, label=r'$\beta$ = {0}'.format(beta))
    
    beta = 0.50
    Es = (q/R**2) * (1 - beta**2)/(1 - beta**2 * np.sin(thetas)**2)**(3/2)
    plt.plot(thetas, Es, label=r'$\beta$ = {0}'.format(beta))

    beta = 0.75
    Es = (q/R**2) * (1 - beta**2)/(1 - beta**2 * np.sin(thetas)**2)**(3/2)
    plt.plot(thetas, Es, label=r'$\beta$ = {0}'.format(beta))

    beta = 0.95
    Es = (q/R**2) * (1 - beta**2)/(1 - beta**2 * np.sin(thetas)**2)**(3/2)
    plt.plot(thetas, Es, label=r'$\beta$ = {0}'.format(beta))
    
    plt.xlabel(r'$\theta$')
    plt.ylabel(r'$E(\theta)$')
    plt.legend(loc='best')
    plt.title('Electric field of a uniformly moving charge')
    plt.savefig('ex2.png')


if __name__ == '__main__':
    main()
