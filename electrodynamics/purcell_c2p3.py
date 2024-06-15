import numpy as np
import matplotlib.pyplot as plt

def varphi(y: float) -> float:
    return -2 * (1/y - 1/np.sqrt(1 + (y - 1)**2))

def plot(ymin: float,
         ymax: float,
         fname: str,
         loc: str='best',
         show_x_axis: bool=True) -> None:
    Y = np.linspace(ymin, ymax)
    V = [varphi(y) for y in Y]
    label = f'In range [{ymin}, {ymax}]'
    plt.plot(Y, V, label=label)
    if show_x_axis:
        plt.hlines(y=0, xmin=ymin, xmax=ymax, color='red')
        
    plt.xlabel(r'$y$')
    plt.ylabel(r'$\varphi(y)$')
    plt.legend(loc=loc)
    plt.savefig(fname)
    plt.close()


def main():
    plot(-2, 2, 'course/purcell_c2p3a.png')
    plot(1.5, 1.7, 'course/purcell_c2p3b.png', show_x_axis=False)   
    plot(0.1, 2, 'course/purcell_c2p3c.png', loc='lower right')
    plot(-5, -0.1, 'course/purcell_c2p3d.png')
    plot(1, 5, 'course/purcell_c2p3e.png')


if __name__ == '__main__':
    main()
