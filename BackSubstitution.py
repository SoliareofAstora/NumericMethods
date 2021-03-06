# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 13:54:56 2017

@author: SoliareOfAstora
"""
import numpy as np

def backSubstitution(source, b, diagonals):
    maxi=np.size(source[0])
    result = np.copy(b);
    for x in range(maxi-1,-1,-1):
        result[x]= (result[x] - source[x,x+1:x+diagonals].dot(result[x+1:x+diagonals]))/source[x,x]
    return result