# -*- coding: utf-8 -*-
"""
Created on Tue May 25 14:51:11 2021

@author: L01268185
"""

import numpy as np

unos=np.ones((3,4))
print (unos)

print()
ceros=np.zeros((4,3))
print (ceros)

print()
aleatorios = np.random.random((2,2))
print(aleatorios)

print()
aleatorios2 = np.random.randint(15, size=(4, 4))
print(aleatorios2)

# Crear una matriz vacía
print()
vacia = np.empty((5,5))
print(vacia)

print()

# Crear una matriz con valores espaciados uniformemente

espacio1 = np.arange(0,30,5)
print(espacio1)

print()

espacio2 = np.linspace(0,2,5)
print(espacio2)

# Conocer las dimensiones de una matriz
a = np.array([(1,2,3),(4,5,6)])
print(a.ndim)

print(a[:, 0:2])


# Encontrar el mínimo, máximo y la suma
a= np.array([2,4,8])
print(a.min())
print(a.max())
print(a.sum())


a = np.array([[1, 2, 3], [4, 5, 6]]) 
b = np.array([[1, 1], [2, 2], [3, 3]]) 
print(a.ndi) 