# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:12:57 2017

@author: SoliareOfAstora
"""
import numpy as np

def forwardSubstitution(source, b):
    
    y = np.zeros(b.size)
    for m, b in enumerate(b.flatten()):
        y[m] = b
        # skip for loop if m == 0
        if m:
            for n in np.xrange(m):
                y[m] -= y[n] * source[m,n]
        y[m] /= source[m, m]
    return y

