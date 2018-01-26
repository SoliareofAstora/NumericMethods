from numpy.polynomial.laguerre import lagroots, Laguerre,poly2lag,lag2poly
import numpy as np

p = np.poly1d([1, 1, 3, 2, -1, -3, -11, -8, -12, -4, 4])
roots = p.roots()

p(-1.33826102e+01)

print(p)
for i in range(roots.size):
    print(p(roots[i]))
print()


p = n.poly1d([1, complex(0, 1), -1, complex(0, -1), 1])
roots = lagroots(p)

print(p)
for i in range(roots.size):
    print(roots[i])



pp=lag2poly(p)
lagroots(pp)
print (p)