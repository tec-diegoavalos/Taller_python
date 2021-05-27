# -*- coding: utf-8 -*-
"""
Created on Tue May 25 17:00:50 2021

@author: L01268185
"""

import numpy as np

data = np.arange(25).reshape(5,5)

temp=data[[0],:]
temp2=data[[1],:]
data[[0],:]=temp2
data[[1],:]=temp

print(data)



data[[0,1],:] = data[[1,0],:]
print(data)

print()

data = np.arange(1,6)
print(data)
print (np.argmax (data)) # Obtiene el índice máximo
data[np.argmax(data)]=0
print(data)



data = np.zeros((5,5))
data += np.arange(1,6)
print(data)



data = np.ones((5,5),dtype=float)

data[:4,:4]=0
data[:1] = 1
data[:,0] =1
print(data)

print()
