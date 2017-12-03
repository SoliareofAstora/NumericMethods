# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 15:14:14 2017

@author: SoliareOfAstora
"""
import numpy as np
from diagonal import Diagonal
from GivensRotation import GivensRotations
from BackSubstitution import backSubstitutuion
#=Prepare Matrix 9x9=========================
d1 = Diagonal()
d1.setNumbers(0, [4, 8, 4, 3, 4, 5, 2, 8, 5])
d0 = Diagonal()
d0.setNumbers(-1, [2, 1, 1, 2, 1, 2, 1, 2])

source = np.zeros((9,9))
source[8,0]=1
source[0,8]=1
for x in range(9):
    source[x,x]=d1.getNumber(x)
    if x>0:
        source[x-1,x]=d0.getNumber(x)
        source[x,x-1]=d0.getNumber(x)   
        
b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

#=Print correct answer with numpy.solve======
CorrectSolve = np.linalg.solve(source,b)   
print("\nsource & numpy solve")
for x in range(9):
    print("x%d"%(x+1),"=%f"%CorrectSolve[x])

#===Sherman-Morrison=========================
u=np.zeros(9)
u[0]=1
u[8]=1
v=u
uvt = np.outer(u, v)
#source = a + uvt
a = source - uvt

for x in range(np.size(a[0])-1):
    G = GivensRotations(a,x)
    a = G.dot(a)
    b = G.dot(b)
    u = G.dot(u)

z=backSubstitutuion(a,b,3)
q=backSubstitutuion(a,u,3)
solve =z- ((v.dot(z)) * q)/(1+v.dot(q))

print("\nShermanMorrison, Givens & back substitution")
for x in range(9):
    print("x%d"%(x+1),"=%f"%solve[x])
