# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 20:58:06 2017

@author: SoliareOfAstora
"""
import numpy as np
from diagonal import Diagonal
from GivensRotation import GivensRotations

#=Prepare Matrix 9x9=========================
d1 = Diagonal()
d1.setNumbers(0, [4, 8, 4, 3, 4, 5, 2, 8, 5])
d0 = Diagonal()
d0.setNumbers(-1, [2, 1, 1, 2, 1, 2, 1, 2])

source = np.zeros((9,9))
for x in range(9):
    source[x,x]=d1.getNumber(x)
    if x>0:
        source[x-1,x]=d0.getNumber(x)
        source[x,x-1]=d0.getNumber(x)
    
b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

#=Calculate correct answer with numpy========
CorrectSolve = np.linalg.solve(source,b)   
print("\nnumpy solve")
for x in range(9):
    print("x%d"%(x+1),"=%f"%CorrectSolve[x])

#=Calculate GivensRotations==================
for x in range(np.size(source[0])-1):
    G = GivensRotations(source,x)
    source= G.dot(source)
    b= G.dot(b)


result = np.zeros(np.shape(b))
maxi = np.size(source[0])-1
result[maxi]=b[maxi]/source[maxi,maxi]
for x in (np.size(source[0])-1,-1,-1):
    for y in (np.size(source[0])-1,x,-1):
        result[x]=b[x]
    


CorrectSolve = np.linalg.solve(source,b)   
print("Correct solve")
for x in range(9):
    print("x%d"%(x+1),"=%f"%CorrectSolve[x])











