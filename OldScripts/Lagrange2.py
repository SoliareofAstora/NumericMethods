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
    xp = np.linspace(-1.4, 2.5, 100)
    _ = plt.plot(xp, result(xp), x, y, ".", )
    plt.savefig('LangrangePlot_' + str(index) + '.png')
    plt.show()


x = np.array([-1.2 ,0.1 ,1.2 ,1.5 ,2.1, 2.2])
y = np.array([-5.9872 ,1.1810, 2.2687, 2.9256 ,5.8354 ,6.6022])

result = np.poly1d(0)
showPlot(0)

for a in range(np.size(x)):
    result += l(x, a) * y[a]

showPlot(a + 1)
print(result)
