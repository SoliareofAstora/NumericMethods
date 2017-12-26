# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:12:57 2017

@author: SoliareOfAstora
"""
import numpy as np
def forwardSubstitution(source, b):
    result=np.copy(b)
    for x in range(0,b.size):
        for y in range(0,x):
            result[x]=result[x]-source[x,y]*result[y]
        result[x]=result[x]/source[x,x]
    return result
