# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 20:58:06 2017

@author: SoliareOfAstora
"""
import math 
import numpy as np
from diagonal import Diagonal
from GivensRotation import GivensRotations



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

G = GivensRotations(a)
a= G.dot(a)
b= G.dot(b)

CorrectSolve = np.linalg.solve(a,b)   
print("Correct solve")
for x in range(9):
    print("x%d"%(x+1),"=%f"%CorrectSolve[x])











