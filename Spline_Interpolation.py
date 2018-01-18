from math import pi, cosh, sinh
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 1 / cosh(pi * x)


def fpp(x):
    return pow(pi, 2) * (2 * pow(sinh(pi * x), 2) - pow(cosh(pi * x), 2)) / pow(cosh(x * pi), 3)


def arrayf(x):
    y = np.array([])
    for i in x:
        y = np.append(y, f(i))
    return y


def arrayfpp(x):
    y = np.array([])
    for i in x:
        y = np.append(y, fpp(i))
    return y


def xn(N):
    x = np.array([])
    for n in range(0, 2 * N + 1):
        x = np.append(x, n / N - 1)
    return x


def yj(i):
    a = np.poly1d([-1, xdim[i + 1]])
    a /= xdim[i + 1] - xdim[i]
    b = np.poly1d([1, -xdim[i]])
    b /= xdim[i + 1] - xdim[i]
    c = (a ** 3 - a) * (xdim[i + 1] - xdim[i]) / 6
    d = (b ** 3 - b) * (xdim[i + 1] - xdim[i]) / 6
    output = a * ydim[i] + b * ydim[i + 1] + c * yppdim[i] + d * yppdim[i + 1]
    return output


N = [2, 5, 32]

for n in range(0, 3):
    xdim = np.array([])
    ydim = np.array([])
    yppdim = np.array([])

    xdim = np.append(xdim, xn(N[n]))
    ydim = np.append(ydim, arrayf(xdim))
    yppdim = np.append(yppdim, arrayfpp(xdim))

    yjdim = np.array([])
    for xi in range(xdim.size - 1):
        yjdim = np.append(yjdim, yj(xi))

    source = np.zeros([xdim.size-2, xdim.size-2])
    for x in range(xdim.size-2):
        source[x, x] = 4
        if x > 0:
            source[x - 1, x] = 1
            source[x, x - 1] = 1

    xp = np.linspace(-1, 1, 1000)
    _ = plt.plot(xp, arrayf(xp), xdim, ydim, ".", alpha=0.3)
    for xi in range(0, xdim.size - 1):
        xp = np.linspace(xdim[xi], xdim[xi + 1], 100)
        temp = yj(xi)
        _ = plt.plot(xp, temp(xp), alpha=0.5)

    plt.show()
