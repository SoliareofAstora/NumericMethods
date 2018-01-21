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


def xn(N):
    x = np.zeros([2 * N + 1])
    for n in range(0, 2 * N + 1):
        x[n] = n / N - 1
    return x


N = np.zeros(16,dtype=int)
for i in range(0,N.size-3):
    N[i]=i+10
N[15]=32
N[14]=2
N[13]=5

xcheck = np.array([])
ycheck = np.array([])
xcheck = xn(500)
ycheck = arrayf(xcheck)

for n in range(0, N.size):
    x = np.array([])
    y = np.array([])
    # Table preparation
    x = xn(N[n])
    y = arrayf(x)


    result = np.poly1d(0)
    for a in range(np.size(x)):
        result += l(x, a) * y[a]

    xp = np.linspace(-1, 1, 1000)
    _ = plt.plot(xp,arrayf(xp),xp,result(xp))
    _ = plt.plot(x,y,".",alpha=0.3)
    plt.ylim(-0.1,1.2)




    check = 0
    for i in range(xcheck.size):
        check += pow(result(xcheck[i])-ycheck[i],2)

    print(str(N[n])+" " + str(check))

    plt.title("nodes: "+str(N[n])+" Error: "+str(check) )
    plt.savefig('plots/Lagrange_N=' + str(N[n]) + '.png')
    plt.show()
