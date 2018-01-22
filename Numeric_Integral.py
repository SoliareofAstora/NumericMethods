import numpy as np
from math import sin, e
import matplotlib.pyplot as plt
import random as rand
from scipy.integrate import romberg





def f(x):
    return sin(x*(x+1))*pow(e,-pow(x,2))


def arrayf(x):
    y = np.zeros([x.size])
    for i in range(x.size):
        y[i] = f(x[i])
    return y



xs = np.array([])
ys = np.array([])

#Table preparation
xs = np.linspace(-1000, 1000, 100000)
ys = arrayf(xs)


xp = np.linspace(-10, 10, 1000)
_ = plt.plot(xp,arrayf(xp))
plt.show()

f(10)

funct = lambda x:f(x)
for i in range(10):
    xs = np.linspace(-(10**i), 10**i, 100000)
    ys = arrayf(xs)

    print ("trapz " + str(np.trapz(ys,xs)))
    print ("romberg " + str(romberg(funct,-(10**i),10**i)))
