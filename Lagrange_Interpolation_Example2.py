# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 09:31:47 2018

@author: Prometeusz
"""
import numpy as np
import matplotlib.pyplot as plt
from math import pi, cosh


def f(x):
    return 1 / cosh(pi * x)


def arrayf(x):
    y = np.zeros([x.size])
    for i in range(x.size):
        y[i] = f(x[i])
    return y


def l(arrx, index):
    poly = np.poly1d(1);
    divider = 1;
    for i in range(np.size(arrx)):
        if i != index:
            poly *= np.poly1d([1, -arrx[i]])
            divider *= arrx[index] - arrx[i]
    return poly / divider


def showPlot(index):
    xp = np.linspace(-1, 1, 100)
    _ = plt.plot(xp, arrayf(xp), alpha=0.3)
    _ = plt.plot(xp, result(xp), x, y, ".", )
    plt.ylim(-0.2, 1.2)
    # plt.savefig('LangrangePlot_' + str(index) + '.png')
    plt.show()


def xn(N):
    x = np.zeros([2 * N + 1])
    for n in range(0, 2 * N + 1):
        x[n] = n / N - 1
    return x


N = [2, 5, 10, 15, 20, 32]

for n in range(0, N.__len__()):
    x = np.array([])
    y = np.array([])
    # Table preparation
    x = xn(N[n])
    y = arrayf(x)

    result = np.poly1d(0)
    for a in range(np.size(x)):
        result += l(x, a) * y[a]
        showPlot(a + 1)


