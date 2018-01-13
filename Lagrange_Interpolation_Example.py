# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 09:31:47 2018

@author: Prometeusz
"""
import numpy as np
import matplotlib.pyplot as plt


def l(arrx, index):
    poly = np.poly1d(1);
    divider = 1;
    for i in range(np.size(arrx)):
        if i != index:
            poly *= np.poly1d([1, -arrx[i]])
            divider *= arrx[index] - arrx[i]
    return poly / divider


def showPlot(index):
    xp = np.linspace(-1, 2, 100)
    _ = plt.plot(xp, result(xp), x, y, ".", )
    plt.ylim(-5, 3)
    plt.savefig('LangrangePlot_' + str(index) + '.png')
    plt.show()


x = np.array([0.0625, 0.1875, 0.3125, 0.4375, 0.5625, 0.6875, 0.8125, 0.9357])
y = np.array([0.67959, 0.073443, -0.517558, -1.07726, -1.60046, -2.08082, -2.50727, -2.86031])

result = np.poly1d(0)
showPlot(0)

for a in range(np.size(x)):
    result += l(x, a) * y[a]
    showPlot(a + 1)
