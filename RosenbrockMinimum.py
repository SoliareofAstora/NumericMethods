import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
import random as rand


def f(x, y):
    return (1 - x ** 2) + 100 * (y - x ** 2) ** 2


def fdx(x, y):
    return 2 * x * (200 * x ** 2 - 200 * y - 1)


def fdy(x, y):
    return 200 * (y - x ** 2)


def arrayf(x, y):
    z = np.zeros([x.size, y.size])
    for i in range(x.size):
        for j in range(y.size):
            z[i, j] = f(x[i], y[j])
    return z


rng = 2
X = np.linspace(-rng, rng, 100)
Y = np.linspace(-rng, rng, 100)
Z = arrayf(X, Y)
epsilon = 1e-15
step = 0.001
prev = 0.3
for i in range(20):

    xy = np.array([rand.uniform(-rng, rng), rand.uniform(-rng, rng)])
    history = np.zeros([2, 2002])
    vector = np.array([0,0])
    a = 0
    history[:, a] = xy
    while True:
        a += 1
        vector = step * np.array([fdx(xy[0], xy[1]), fdy(xy[0], xy[1])])+prev *vector
        xy -= vector

        history[:, a] = xy

        # if f(xy[0], xy[1]) < epsilon or
        if a > 2000:
            break

    plt.pcolor(X, Y, Z, norm=LogNorm(10))
    plt.colorbar()
    plt.plot(history[1, :a], history[0, :a], color="red")
    plt.plot(history[1, 0], history[0, 0], ".")
    plt.title(str(a) + " steps  Momentum f(x) = " + str(f(xy[0], xy[1])))
    print(str(f(xy[0], xy[1])))
    plt.savefig('plots/rosenbergMinimalization' + str(i) + '.png')
    plt.clf()
