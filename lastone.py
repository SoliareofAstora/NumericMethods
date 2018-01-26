from numpy.polynomial.laguerre import lagroots
import numpy as n

p = n.poly1d([1, 1, 3, 2, -1, -3, -11, -8, -12, -4, 4])
roots = lagroots(p)

print(p)
for i in range(roots.size):
    print(roots[i])
print()

p = n.poly1d([1, complex(0, 1), -1, complex(0, -1), 1])
roots = lagroots(p)

print(p)
for i in range(roots.size):
    print(roots[i])
