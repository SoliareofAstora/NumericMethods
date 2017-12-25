# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 20:58:06 2017

@author: SoliareOfAstora
"""
import numpy as np
from GivensRotation import GivensRotations
#=Prepare Matrix 9x9=========================
b = np.array([1., 2, 3, 4, 5, 6, 7, 8, 9])
d3 = np.zeros((8))
d2 = np.array([2., 1, 1, 2, 1, 2, 1, 2, 0])
d1 = np.array([4., 8, 4, 3, 4, 5, 3, 8, 5])
d0 = np.array([2., 1, 1, 2, 1, 2, 1, 2])
    
#=Calculate GivensRotations==================
for x in range(8):
    ta = np.array([[d1[x],d2[x]],[d0[x],d1[x+1]]])
    G = GivensRotations(ta,0)
    ta = G.dot(ta)
    d3[x] = G[0,1]*d2[x+1]
    d2[x+1] = G[1,1]*d2[x+1]
    d1[x] = ta[0,0]
    d2[x] = ta[0,1]
    d1[x+1]=ta[1,1]
    
    temp = b[x]
    b[x] = G[0,0]*b[x]+G[0,1]*b[x+1]
    b[x+1] = G[1,0]*temp+G[1,1]*b[x+1]
    

#=Solve rotated matrix with backsubstitution=
b[8] = b[8]/d1[8]
b[7] = (b[7] - d2[7]*b[8])/d1[7]

for x in range(6,-1,-1):
    b[x]= (b[x] - (d3[x]*b[x+2]+d2[x]*b[x+1]))/d1[x]
  
print("\nGivens & back substitution")
for x in range(9):
    print("x%d"%(x+1),"=%f"%b[x]) #result[x])