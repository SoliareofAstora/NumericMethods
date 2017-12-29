# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 17:08:12 2017

@author: SoliareOfAstora
"""
import numpy as np

class diagonalArray:
    values = np.array([8,2,1])
    offset = np.array([0,1,3])
    
    def getValue(self, x , y):
        distance = x - y;
        if distance < 0: 
            distance *= -1;
        for i in range(np.size(self.offset)):
            if self.offset[i]==distance:
                return self.values[i]
        return 0;
        
arr = diagonalArray
diagonalArray.getValue(arr,2,2)
