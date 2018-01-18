from math import sin
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x*(x**2-1)*sin(x)**2

def arrayf(x):
    y = np.zeros([x.size])
    for i in range(x.size):
        y[i] = f(x[i])
    return y


xp = np.linspace(-10, 10, 1000)
_ = plt.plot(xp, arrayf(xp))
plt.show()
