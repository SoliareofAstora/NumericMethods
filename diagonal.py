# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 21:02:09 2017

@author: SoliareOfAstora
"""
import numpy as np

class Diagonal:
    x = np.array([])
    row = 0

    def setNumbers(self, rownumber, vector):
        self.x = vector
        self.row = rownumber

    def getNumber(self, rownumber):
        temp = rownumber + self.row
        if temp >= 0:
            if temp < np.size(self.x):
                return self.x[temp]
            else:
                return 0
        else:
            return 0

