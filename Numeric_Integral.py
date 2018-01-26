import numpy as np
from math import *
import matplotlib.pyplot as plt
from scipy.integrate import romberg, trapz


def f(x):
    return sin(x * (x + 1)) * pow(e, -pow(x, 2))


def arrayf(x):
    y = np.zeros([x.size])
    for i in range(x.size):
        y[i] = f(x[i])
    return y


epsilon = 1e-8

Range = 0

while True:
    Range += 1
    value = pow(e, -pow(Range, 2))
    if value < epsilon:
        Range -= 1
        break

xp = np.linspace(-Range, Range, 100000)
yp = arrayf(xp)
plt.plot(xp, yp)

print("trapz " + str(trapz(yp, xp)))
print("romberg " + str(romberg(lambda x: f(x), -Range, Range, tol=epsilon)))

plt.show()
