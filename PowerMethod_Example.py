# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 17:08:12 2017

@author: SoliareOfAstora
"""
import numpy as np

class diagonalArray:
    values = np.array([8,2,1])
    offset = np.array([0,1,3])
    
    def get(self, x , y):
        if y<0: 
            return 0
        distance = x - y;
        if distance < 0: 
            distance *= -1;
        for i in range(np.size(self.offset)):
            if self.offset[i]==distance:
                return self.values[i]
        return 0
        
    def calculate(self,source,output):
        for i in range(64):
            output[i] = 0
            for j in range(-3,4,1):
                if (i+j>=0 and i+j<64):
                    output[i] += self.get(self,i,i+j)*source[i+j]
            
arr = diagonalArray
srr = np.ones((64))
wrr = np.ones((64))
result = np.zeros((10000,64))
for i in range(10000):
    wrr = wrr/np.linalg.norm(wrr)
    srr=np.copy(wrr)
    result[i]=np.copy(wrr)
    diagonalArray.calculate(arr,srr,wrr)
    