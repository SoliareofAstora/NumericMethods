# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 20:58:06 2017

@author: SoliareOfAstora
"""
from diagonal import Diagonal
import numpy as np
import math

def distance(p0, p1):
    return math.sqrt((p0)**2 + (p1)**2)

def Givens(source,x):
    (rows, cols)=np.shape(source)
    
    r = distance(source[x,x],source[x+1,x])
    c = source[x,x] / r
    s = -source[x+1,x] / r
    
    G=np.identity(9)
    G[x, x] = c
    G[x + 1, x + 1] = c
    G[x + 1, x] = s
    G[x, x + 1] = -s

    return G

#=====Prepare Matrix=========================
d1 = Diagonal()
d1.setNumbers(0, [4, 8, 4, 3, 4, 5, 2, 8, 5])
d0 = Diagonal()
d0.setNumbers(-1, [2, 1, 1, 2, 1, 2, 1, 2])
b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

source = np.zeros((9,9))
for x in range(9):
    source[x,x]=d1.getNumber(x)
    if x>0:
        source[x-1,x]=d0.getNumber(x)
        source[x,x-1]=d0.getNumber(x)
#============================================

#=====Correct answer ========================
CorrectSolve = np.linalg.solve(source,b)   
print("Correct solve")
for x in range(9):
    print("x%d"%(x+1),"=%f"%CorrectSolve[x])
#============================================

    
a = np.copy(source)


for x in range(8):
    G = Givens(a,x)
    a= G*a
    b= G.dot(b)

CorrectSolve = np.linalg.solve(a,b)   
print("Correct solve")
for x in range(9):
    print("x%d"%(x+1),"=%f"%CorrectSolve[x])











