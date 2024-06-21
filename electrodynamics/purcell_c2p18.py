import numpy as np
import matplotlib.pyplot as plt

a = 1
b = 1
sigma = 4/np.pi # Chosen so that 4\pi\sigma a = 1 !!
K = 4*np.pi*sigma*a

def E_field(z: float) -> float:
    return K*((4*a**2+(b-2*z)**2)**(-1/2)+\
              (4*a**2+(b+2*z)**2)**(-1/2))

def main():
    Z = np.linspace(-4*b, 4*b, 200)
    E = [E_field(z) for z in Z]
    plt.plot(Z, E)
    plt.axvline(x=-b/2, ls='--')
    plt.axvline(x=b/2, ls='--')
    plt.xlabel(r'$z$')
    plt.ylabel(r'$E(z)$')
    plt.title('Electric field in a charged cylinder')
    plt.savefig('course/purcell_c2p18.png')


if __name__ == '__main__':
    main()
    
