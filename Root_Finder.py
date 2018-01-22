from math import sin
import numpy as np
import matplotlib.pyplot as plt
import random as rand
from scipy.interpolate import CubicSpline, interp1d


# (Obowiązkowe) Dane jest równanie
# x(x2 − 1) sin2(x) = 0.
# Rozwiąż równanie stosując algorytm siecznych i algorytm oparty o trzypunktową interpolację
# odwrotną statrując odpowiednio z dwóch i trzech punktów losowych z przedziału (0, 1). Punkty
# początkowe dla metody siecznych mają być dwoma z trzech punktów startowych dla algorytmu
# opartego o interpolację odwrotną. Wyznacz miejsca zerowe z dokładnością 10−8.
# Rozwiązanie powinno zawierać:
#  - krótki opis obu metod i ich implementację
#  - porównanie szybkości zbieżności obu metod dla 20 zestawów punktów startowych


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
    sortorder = np.argsort(array, kind='mergesort', axis=1)
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
            iterator -= 1
            ItsOK = False
            break
        tmp = cubic(0)
        interxy = np.append(interxy, np.array([[tmp], [f(tmp)]]), axis=1)

        if f(tmp-epsilon/2)*f(tmp+epsilon/2)<0:
            break

    if ItsOK:
        # metoda secznych
        sieczxy = sortX(xystart[:, (0, 1)])
        iter = 0
        while True:
            sieczna = np.poly1d(np.polyfit(sieczxy[0,iter:iter+2], sieczxy[1,iter:iter+2], 1))
            temp = sieczna(0)
            sieczxy = np.append(sieczxy, np.array([[temp], [f(temp)]]), axis=1)
            iter+=1

            if f(temp-epsilon/2)*f(temp+epsilon/2)<0:
                break
    if ItsOK:
        print()
        print(interCounter, tmp, f(tmp))
        print(iter, temp, f(temp))
        xp = np.linspace(-0.01,1.01,10000)
        plt.plot(xp, arrayf(xp))
        plt.plot(xystart[0], xystart[1], "+", label="punkty Startowe")
        plt.plot(interxy[0], interxy[1], "." ,alpha=0.5,label="odwrotna Innterpolacja")
        plt.plot(sieczxy[0], sieczxy[1], ".",alpha=0.5, label = "Metoda siecznych")
        plt.legend()
        plt.show()


    if iterator >= 4:
        break

        # xp = np.linspace(-1.01, 1.01, 1000)
        # plt.plot(xp, arrayf(xp))
        # # plt.plot(xp, cubic(xp))
        # # plt.plot(xystart[0], xystart[1], ".")
        # plt.plot(cubxy[0], cubxy[1], ".")
        # plt.plot(xp, xp * 0, alpha=0.3)
        # plt.ylim(-0.25, 0.25)
        # plt.show()
