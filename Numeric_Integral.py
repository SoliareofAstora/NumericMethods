import numpy as np
from math import *
import matplotlib.pyplot as plt
from scipy.integrate import romberg, quadrature,cumtrapz, simps, romb


def f(x):
    return sin(x*(x+1))*pow(e,-pow(x,2))


def arrayf(x):
    y = np.zeros([x.size])
    for i in range(x.size):
        y[i] = f(x[i])
    return y


xp = np.linspace(-5, 5, 1000)
# _ = plt.plot(xp,arrayf(xp))


f(1030)

funct = lambda x:f(x)
arrfunct = lambda x:arrayf(x)
for i in range(1,15):
    step = 10**i
    # xs = np.linspace(-step, step, step**2)
    # ys = arrayf(xs)

    print ("10^"+str(i))
    # print ("trapz " + str(np.trapz(ys,xs)))
    # print(" cumtrapz " + str(cumtrapz(ys, xs)))
    print ("quadrature "+str(
        quadrature(arrfunct,-step,step)
    ))
    print ("romberg " + str(romberg(funct,-step,step,tol=1e-8,divmax=40)))


    # plt.plot(xs,ys,".")
    # plt.xlim(-4,4)
    # plt.show()

