import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
import random as rand


def f(x, y):
    return (1 - x)**2 + 100 * (y - x ** 2) ** 2


def fdx(x, y):
    return 2*(200 * x ** 3 - 200 * x * y + x - 1)


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
epsilon = 1e-8
step = 0.001
prev = 0.5
for i in range(20):

    xy = np.array([rand.uniform(-rng, rng), rand.uniform(-rng, rng)])
    history = np.empty(2)
    vector = np.array([0,0])
    a = 0
    history =xy
    while True:
        a += 1
        vector = np.array([fdx(xy[0], xy[1]), fdy(xy[0], xy[1])])+prev *vector
        xy -= step*vector

        history = np.append(history, xy)

        distance = np.linalg.norm(xy-[1,1])
        if distance < epsilon or distance>100:
            break

    plt.pcolor(X, Y, Z, norm=LogNorm(10))

    plt.plot(history[1::2], history[0::2])#,# color="red")
    plt.plot(history[1], history[0], ".")
    plt.title(str(a) + " steps  Momentum f(x) = " + str(f(xy[0], xy[1])))
    print(str(f(xy[0], xy[1])))
    plt.savefig('plots/rosenbergMinimalization' + str(i) + '.png')

    plt.colorbar()
    plt.clf()

