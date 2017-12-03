# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:44:09 2017

@author: SoliareOfAstora
"""

import numpy as np
import scipy
from ForwardSubstitution import forwardSubstitution
from BackSubstitution import backSubstitution

a = np.array([[-676.666,163.335,-66.6671,-26.6912,-9.35915],
              [163.335,443.333,-466.666,-186.837,-65.5135],
              [-66.6671,-466.666,133.338,-266.91,-3.5908],
              [-26.6912,-186.837,-266.91,-457.663,-405.929],
              [-9.35915,-65.5135,-93.5908,-405.929,557.663]])
    
b = np.array([[-0.915304,0.663939,-0.985599,-1.14813,0.657107],
              [-0.915304,0.663939,-0.985599,-1.15144,0.666543],
              [0.145357,1.01749,-0.278492,-1.28907,-0.452008],
              [0.145357,1.01749,-0.278492,-1.29379,-0.453663]])
    
properSolve=np.zeros((4,5))
for x in range(0,4):
    properSolve[x,:] = np.linalg.solve(a,b[x])  



Permutation,Lower,Upper = scipy.linalg.lu(a)
for x in range(0,4):
    b[x]=b[x].dot(Permutation)


Solve=np.zeros((4,5))
for x in range(0,4):
    y = forwardSubstitution(Lower,b[x])
    Solve[x,:] = backSubstitution(Upper,y,5)
    
    
