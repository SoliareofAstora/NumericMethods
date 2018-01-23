import numpy as np
from math import *
import matplotlib.pyplot as plt
from scipy.integrate import romberg, quadrature


def f(x):
    return sin(x*(x+1))*pow(e,-pow(x,2))


def arrayf(x):
    y = np.zeros([x.size])
    for i in range(x.size):
        y[i] = f(x[i])
    return y


def trapezint(f, a, b, n):
    h = (b - a) / n
    sum = 0
    part1 = (0.5) * h * (f(a) + f(b))
    for i in range(1, n):
        xi = a + i * h
        sum = sum + f(xi)
    return part1 + h * sum


def adaptivetrap(f, a, b, ep):
    max = 0
    step = float(abs(a - b) / 1000)
    i = 0
    while (i < 1000):
        i = i + 1
        adj = a;
        adj = a + step * i;
        dval = diff2(f, adj)
        if (abs(dval) > max):
            max = abs(dval)

    h = sqrt(12 * ep) * ((b - a) * max) ** .5
    n = (b - a) / h
    return trapezint(f, a, b, int(ceil(n)))


print
adaptivetrap(f1, 0.0, 10.0, 1E-5)

xp = np.linspace(-5, 5, 1000)
_ = plt.plot(xp,arrayf(xp))
plt.show()

f(10)

funct = lambda x:f(x)
arrfunct = lambda x:arrayf(x)
for i in range(1,10):
    xs = np.linspace(-(10**i), 10**i, 10023)
    ys = arrayf(xs)

    print (10**i)
    print ("trapz " + str(np.trapz(ys,xs)))
    print ("quadrature "+str(
        quadrature(arrfunct,-(10**i),10**i)
    ))
    print ("romberg " + str(romberg(funct,-(10**i),10**i)))


dlalex=89+102+61
dlalex/2