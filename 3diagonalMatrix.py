# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 20:58:06 2017

@author: SoliareOfAstora
"""
from diagonal import Diagonal
import numpy as np
import math

def Givens(source,x):
    r=math.sqrt(math.pow(source[x,x],2)+math.pow(source[x + 1,x],2))
    c=source[x , x] / r
    s=source[x + 1,x] / r
    output = np.zeros(np.shape(source))
    np.fill_diagonal(output,1)
    output[x,x]=c
    output[x + 1, x + 1] = c
    output[x + 1, x] = -s
    output[x, x + 1] = s
    return output




#=====Prepare Matrix=========================
d1 = Diagonal()
d1.setNumbers(0, [4, 8, 4, 3, 4, 5, 2, 8, 5])
d0 = Diagonal()
d0.setNumbers(-1, [2, 1, 1, 2, 1, 2, 1, 2])
b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
a = np.zeros((9,9))
for x in range(9):
    a[x,x]=d1.getNumber(x)
    if x>0:
        a[x-1,x]=d0.getNumber(x)
        a[x,x-1]=d0.getNumber(x)
#============================================

#=====Correct answer 
CorrectSolve = np.linalg.solve(a,b)   

print("Correct solve")
for x in range(9):
    print("x%d"%(x+1),"=%f"%CorrectSolve[x])
    

#Givens(a,3)
