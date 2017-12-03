# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 13:54:56 2017

@author: SoliareOfAstora
"""
import numpy as np

def backSubstitutuion(source, b, diagonals):
    #result = np.ones(np.shape(b))
    maxi=np.size(source[0])
    for x in range(maxi-1,-1,-1):
        b[x]= (b[x] - source[x,x+1:x+diagonals].dot(b[x+1:x+diagonals]))/source[x,x]
    return b