# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:12:57 2017

@author: SoliareOfAstora
"""

def forwardSubstitution(source, b):
    
    for x in range(0,b.size):
        for y in range(0,x):
            b[x]=b[x]-source[x,y]*b[y]
        b[x]=b[x]/source[x,x]
    return b
