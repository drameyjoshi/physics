import numpy as np
import matplotlib.pyplot as plt

from functools import partial
from scipy.optimize import fsolve

def F(a, x, y):
    return 1/(2 * a) - 1/np.sqrt((x - a)**2 + y**2) - 1/np.sqrt((x + a)**2 + y**2)

a_curve = partial(F, 1)

a = 1
X = np.linspace(-4, 4, 1000)
Y = []

for x in X:
    roots = fsolve(a_curve, a, x)
    Y.append(roots[0])

Xs = X.tolist()
Xs.extend(Xs)
Ys = Y + [-y for y in Y]

plt.scatter(Xs, Ys, s = 1)
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.title(r'$F(a=1, x, y) = 0$')
plt.savefig('purcell_c1p7.png')
plt.show()
