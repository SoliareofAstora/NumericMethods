# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:12:57 2017

@author: SoliareOfAstora
"""
import numpy as np

def forwardSubstitutuion(source, b, diagonals):
    
    maxi=np.size(source[0])
    for x in range(0,maxi-1,):
        b[x]= (b[x] - source[x,x-diagonals:x].dot(b[x-diagonals:x]))/source[x,x]
    return b


