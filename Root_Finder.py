from math import sin
import numpy as np
import random as rand
from scipy.interpolate import CubicSpline


def f(x):
    return x * (x ** 2 - 1) * (sin(x)) ** 2


def arrayf(x):
    y = np.zeros([x.size])
    for i in range(x.size):
        y[i] = f(x[i])
    return y


def sortX(array):
    sortorder = np.argsort(array, axis=1)
    sortx = np.zeros(array.shape)
    for i in range(sortorder[1].size):
        sortx[:, i] = array[:, sortorder[0][i]]
    return sortx


def sortY(array):
    sortorder = np.argsort(array, axis=1)
    sorty = np.zeros(array.shape)
    for i in range(sortorder[1].size):
        sorty[:, i] = array[:, sortorder[1][i]]
    return sorty


epsilon = pow(10, -8)
iterator = 0
ItsOK = False
while True:

    iterator += 1
    ItsOK = True
    xystart = np.zeros((2, 3))
    for i in range(0, 3):
        xystart[0, i] = rand.uniform(0, 1)
        xystart[1, i] = f(xystart[0, i])

    # odwrotna interpolacja
    interxy = np.copy(xystart)
    interCounter = 0
    while True:
        interCounter += 1
        interxy = sortY(interxy)
        try:
            cubic = CubicSpline(interxy[1], interxy[0])
        except ValueError:
            # czasami sortowanie punktów zawodzi powodując błąd interpolacji.
            # dlatego też odrzucam trójkę punktów które spowodowały błąd
            # cofając główny index iteracji o jeden oraz
            # pomijając metodę siecznych i rysowanie wyników
            iterator -= 1
            ItsOK = False
            break
        tmp = cubic(0)
        interxy = np.append(interxy, np.array([[tmp], [f(tmp)]]), axis=1)

        if f(tmp - epsilon / 2) * f(tmp + epsilon / 2) < 0:
            break

    if ItsOK:
        # metoda secznych
        sieczxy = sortX(xystart[:, (0, 1)])
        iter = 0
        while True:
            sieczna = np.poly1d(np.polyfit(sieczxy[0, iter:iter + 2], sieczxy[1, iter:iter + 2], 1))
            temp = -sieczna[0]/sieczna[1]
            sieczxy = np.append(sieczxy, np.array([[temp], [f(temp)]]), axis=1)
            iter += 1

            if f(temp - epsilon / 2) * f(temp + epsilon / 2) < 0:
                break
    if ItsOK:
        print("odwrotna interpolacja")
        print(interCounter, tmp, f(tmp))
        print("metoda siecznych")
        print(iter, temp, f(temp))
        print()

        # xp = np.linspace(-0.01,1.01,10000)
        # plt.plot(xp, arrayf(xp))
        # plt.plot(xystart[0], xystart[1], "+", label="punkty Startowe")
        # plt.plot(interxy[0], interxy[1], "." ,alpha=0.5,label="odwrotna Innterpolacja")
        # plt.plot(sieczxy[0], sieczxy[1], ".",alpha=0.5, label = "Metoda siecznych")
        # plt.legend()
        # plt.show()

    if iterator >= 20:
        break
