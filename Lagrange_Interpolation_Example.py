# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 09:31:47 2018

@author: Prometeusz
"""
import numpy as np
def l(arrx,arry,index):
    tempa=1;
    tempb=1;
    for i in range(np.size(arrx)):
        if  i !=index:
            tempa*=-arry[i]
            tempb*=arrx[index] - arry[i]
    return tempa/tempb

x=np.array([0.0625,0.1875,0.3125,0.4375,0.5625,0.6875,0.8125,0.9357])
y=np.array([0.67959,0.073443,-0.517558,-1.07726,-1.60046,-2.08082,-2.50727,-2.86031])


for z in range(np.size(x)):
    l(x,y,z)