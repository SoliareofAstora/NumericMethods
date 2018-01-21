from math import pi, cosh, sinh
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 1 / cosh(pi * x)


def fpp(x):
    return pow(pi, 2) * (2 * pow(sinh(pi * x), 2) - pow(cosh(pi * x), 2)) / pow(cosh(x * pi), 3)


def arrayf(x):
    y = np.zeros([x.size])
    for i in range(x.size):
        y[i] = f(x[i])
    return y


def arrayfpp(x):
    y = np.zeros([x.size])
    for i in range(x.size):
        y[i] = fpp(x[i])
    return y


def xn(N):
    x = np.zeros([2 * N + 1])
    for n in range(0, 2 * N + 1):
        x[n] = n / N - 1
    return x


def yj(i):
    a = np.poly1d([-1, xdim[i + 1]])
    a /= xdim[i + 1] - xdim[i]
    b = np.poly1d([1, -xdim[i]])
    b /= xdim[i + 1] - xdim[i]
    c = (a ** 3 - a) * (xdim[i + 1] - xdim[i]) / 6
    d = (b ** 3 - b) * (xdim[i + 1] - xdim[i]) / 6
    output = a * ydim[i] + b * ydim[i + 1] + c * yppdim[i] + d * yppdim[i + 1]
    ppoutput = a*yppdim[i]+b*yppdim[i+1]
    return output, ppoutput


N = [2, 5, 32]

for n in range(0, 3):
    # n=0
    xdim = np.array([])
    ydim = np.array([])
    yppdim = np.array([])

    #Table preparation
    xdim = xn(N[n])
    ydim = arrayf(xdim)
    yppdim = arrayfpp(xdim)

    yjdim = np.empty((xdim.size-1),dtype=np.poly1d)#Functions
    yjppdim = np.empty((xdim.size-1),dtype=np.poly1d)#PFunctions
    for xi in range(xdim.size - 1):
        yjdim[xi],yjppdim[xi] = yj(xi)

    a = np.zeros([xdim.size-2, xdim.size-2])
    for x in range(xdim.size-2):
        a[x, x] = 4
        if x > 0:
            a[x - 1, x] = 1
            a[x, x - 1] = 1

    vector = np.zeros([xdim.size-2])
    for i in range (xdim.size-2):
        vector[i]=(ydim[i]-2*(ydim[i+1])+ydim[i+2])*(6/pow(xdim[1] - xdim[0],2))

    out = np.linalg.solve(a,vector)

    # for i in range(1,xdim.size-3):
        # yjdim[i-1][4] = (out[i]-out[i-1])
        # yjdim[i][4] = (out[i+1] - out[i])


    xp = np.linspace(-1, 1, 1000)
    _ = plt.plot(xp, arrayf(xp), xdim, ydim, ".", alpha=0.3)
    _ = plt.plot(xp, xp*0,alpha=0.1)
    for xi in range(0, xdim.size - 1):
        xp = np.linspace(xdim[xi], xdim[xi + 1], 100)
        _ = plt.plot(xp, yjdim[xi](xp), alpha=0.5)
       # _ = plt.plot(xp, yjdim[xi].deriv(1)(xp), alpha=0.5)
        # _ = plt.plot(xp, yjdim[xi].deriv(2)(xp), alpha=0.5)

    plt.show()
