# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:44:09 2017

@author: SoliareOfAstora
"""

import numpy as np
import scipy
from ForwardSubstitution import forwardSubstitution
from BackSubstitution import backSubstitution

#=Prepare Matrix=============================
asource = np.array([
              [-676.666,163.335,-66.6671,-26.6912,-9.35915],
              [163.335,443.333,-466.666,-186.837,-65.5135],
              [-66.6671,-466.666,133.338,-266.91,-3.5908],
              [-26.6912,-186.837,-266.91,-457.663,-405.929],
              [-9.35915,-65.5135,-93.5908,-405.929,557.663]])
    
bsource = np.array([
              [-0.915304,0.663939,-0.985599,-1.14813,0.657107],
              [-0.915304,0.663939,-0.985599,-1.15144,0.666543],
              [0.145357,1.01749,-0.278492,-1.28907,-0.452008],
              [0.145357,1.01749,-0.278492,-1.29379,-0.453663]])

a=np.copy(asource)
b=np.copy(bsource)

properSolve = np.zeros((4,5))
for x in range(0,4):
    properSolve[x,:] = np.linalg.solve(a,b[x])  

#===LU factorization
#I might implement LU with this solution
#https://www.quantstart.com/articles/LU-Decomposition-in-Python-and-NumPy
Permutation,Lower,Upper = scipy.linalg.lu(a)
for x in range(0,4):
    b[x]=b[x].dot(Permutation)




z = np.zeros((4,5))
for x in range(0,4):
    print("b%d"%(x+1))
    z[x,:] = backSubstitution(Upper,forwardSubstitution(Lower,b[x]),5)
    for y in range(5):
        print("x%d"%(y+1),"=%f"%z[x,y])
        
    
    
    
b=np.copy(bsource)
np.linalg.norm(a)*np.linalg.norm(np.linalg.inv(a))/2

np.linalg.norm(b[0]-b[1])
A_1dB = backSubstitution(Upper,forwardSubstitution(Lower,b[0]-b[1]),5)
minwlasna=1/min(np.linalg.eigvals(a))

np.linalg.norm(b[2]-b[3])
np.linalg.norm(z[0]-z[1])/np.linalg.norm(b[0]-b[1])
np.linalg.norm(z[2]-z[3])/np.linalg.norm(b[2]-b[3])

(np.linalg.norm(z[0]-z[1])/np.linalg.norm(b[0]-b[1]))*(np.linalg.norm(b[1])/np.linalg.norm(z[1]))
(np.linalg.norm(z[2]-z[3])/np.linalg.norm(b[2]-b[3]))*(np.linalg.norm(b[3])/np.linalg.norm(z[3]))

np.linalg.cond(a)

np.linalg.norm(b[0]-b[1])