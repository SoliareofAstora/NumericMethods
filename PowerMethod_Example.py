# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 17:08:12 2017

@author: SoliareOfAstora
"""
import numpy as np

class diagonalArray:
    values = np.array([8,2,1])
    diagonals = np.array([0,1,3])
    
    def getValue(self, x , y):
        distace = x - y;
        if distance < 0: 
            distance *= -1;
        
