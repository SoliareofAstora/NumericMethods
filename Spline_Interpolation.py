from math import pi, cosh
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline


def f(x):
    return 1 / cosh(pi * x)


def arrayf(x):
    y = np.zeros([x.size])
    for i in range(x.size):
        y[i] = f(x[i])
    return y


def xn(N):
    x = np.zeros([2 * N + 1])
    for n in range(0, 2 * N + 1):
        x[n] = n / N - 1
    return x


N = np.array([2,3,4, 5, 32])
xcheck = np.array([])
ycheck = np.array([])
xcheck = xn(500)
ycheck = arrayf(xcheck)

for n in range(0, N.size):

    xs = np.array([])
    ys = np.array([])

    #Table preparation
    xs = xn(N[n])
    ys = arrayf(xs)

    splines = CubicSpline(xs,ys)

    xp = np.linspace(-1, 1, 1000)
    _ = plt.plot(xp,arrayf(xp),xp,splines(xp))
    _ = plt.plot(xs,ys,".",alpha=0.3)
    plt.show()

    check = 0
    for i in range(xcheck.size):
        check += pow (splines(xcheck[i])-ycheck[i],2)

    print(check)

