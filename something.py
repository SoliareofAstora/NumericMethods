import numpy as np
from scipy.integrate import romberg
import math
import matplotlib.pyplot as plt


def f(x):
    return math.sin(x*(x+1))*pow(math.e,-pow(x,2))

precision = 1.0e-8
init = 0
bound_1 = -100
bound_2 = 100

#Znajdowanie górnej granicy całkowania
while True:
    init = pow(math.e,-pow(bound_2,2))
    if init > precision:
        # bound_2 = bound_2 + 1
        break
    bound_2 = bound_2 - 1

#Znajdowanie dolnej granicy całkowania
while True:
    init = pow(math.e,-pow(bound_1,2))
    if init > precision:
        #bound_1 = bound_1 - 1
        break
    bound_1 = bound_1 + 1

print("Granice całkowania: ")
limits = np.array([bound_1, bound_2])
print(limits)
print()
#Używamy metody Romberga
print("Całka Romberga")
print(romberg(f,bound_1,bound_2, divmax=19))

def trapezoidal(func, lBound, uBound):
    cont = (uBound-lBound)
    ans = 0.5*func(lBound) + 0.5*func(uBound)
    j = 1
    ansPrev = 1
    AnsConv = np.empty([1])
    AnsConv[0] = 1
    while True:
        cont = cont/2.0
        #Pętla z przedziałem od 1 do liczby paneli
        for i in range(1, np.power(2, (j-1))):
            ans = ans + func((lBound + (2*i-1)*cont))
        temp = ans * cont
        AnsConv = np.insert(AnsConv, j, temp)
        if np.abs(ansPrev - temp) < precision:
            break
        ansPrev = AnsConv[j]
        print(AnsConv[j])
        j = j + 1
    print(AnsConv[j])

print()
print("Trapezoidal result:")
res = trapezoidal(f, bound_1, bound_2)
print(res)
