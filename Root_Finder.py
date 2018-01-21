from math import sin
import numpy as np
import matplotlib.pyplot as plt

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
    return x*(x**2-1)*sin(x)**2

def arrayf(x):
    y = np.zeros([x.size])
    for i in range(x.size):
        y[i] = f(x[i])
    return y


xp = np.linspace(-10, 10, 1000)
_ = plt.plot(xp, arrayf(xp))
plt.show()
