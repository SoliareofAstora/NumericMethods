# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 20:58:06 2017

@author: SoliareOfAstora
"""
import numpy as np
from diagonal import Diagonal
from GivensRotation import GivensRotations
from BackSubstitution import backSubstitution
#=Prepare Matrix 9x9=========================
b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
d3 = np.zeros((7))
d2 = np.array([2, 1, 1, 2, 1, 2, 1, 2])
d1 = np.array([4, 8, 4, 3, 4, 5, 3, 8, 5])
d0 = np.array([2, 1, 1, 2, 1, 2, 1, 2])


#=Print correct answer with numpy.solve======
source = np.zeros((9,9))
for x in range(9):
    source[x,x]=d1[x]
    if x>0:
        source[x-1,x]=d0[x-1]
        source[x,x-1]=d2[x-1]
CorrectSolve = np.linalg.solve(source,b)   
print("\nsource & numpy solve")
for x in range(9):
    print("x%d"%(x+1),"=%f"%CorrectSolve[x])
    
#=Calculate GivensRotations==================
for x in range(8):
    ta = np.array([[d1[x],d2[x]],[d0[x],d1[x+1]]])
    G = GivensRotations(ta,0)
    ta = G.dot(ta)
    tb = np.array(b[])
    b = G.dot(b)
    
#=Solve rotated matrix with backsubstitution=
result = backSubstitution(source, b,3)
print("\nGivens & back substitution")
for x in range(9):
    print("x%d"%(x+1),"=%f"%result[x])