import matplotlib.pyplot as plt
import numpy as np

def nth_term(n: int) -> float:
    d = 2
    s = 1
    x = 4*n*(1/np.sqrt(d**2 + (2*n)**2) - 1/np.sqrt(d**2 + (2*(n - 1))**2))
    return x


def show_plots(X: np.array,
               contribs: np.array,
               U: np.array) -> None:
    plt.plot(X, U, label=r'$U(n)$')
    plt.plot(X, contribs, label=r'$\delta U(n)$')    
    plt.xlabel('n')
    plt.title(r'Potential energy of 2-d lattice')
    plt.legend(loc='best')
    plt.savefig('purcell_c1p27.png')


def convergence(n: int) -> None:
    template = 'At n={0:.0e}, the additional contribution to U is {1:f}.'
    print(template.format(n, nth_term(n)))


def main():
    N = 1000
    contribs = [nth_term(n) for n in range(1, N + 1)]
    U = np.cumsum(contribs)
    X = [n for n in range(1, N + 1)]
    show_plots(X, contribs, U)
    convergence(1e6)
    convergence(1e23)
    

if __name__ == '__main__':
    main()
