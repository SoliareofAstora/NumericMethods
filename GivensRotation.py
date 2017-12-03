# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 21:06:51 2017

@author: SoliareOfAstora
"""
import numpy as np
from math import sqrt

def GivensRotations(source,x):
    #G=np.identity(np.size(source[0]))
    #for x in range(np.size(source[0])-1):
    r = sqrt((source[x,x])**2 + (source[x+1,x])**2)
    cos = source[x,x] / r
    sin = -source[x+1,x] / r
    Gt=np.identity(np.size(source[0]))
    Gt[x, x] = cos
    Gt[x + 1, x + 1] = cos
    Gt[x + 1, x] = sin
    Gt[x, x + 1] = -sin
     #   G=Gt.dot(G)
    return Gt #G