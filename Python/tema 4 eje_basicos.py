# -*- coding: utf-8 -*-
"""
Created on Tue May 25 17:35:59 2021

@author: L01268185
"""

import numpy as np

print ('::: Ejercicios Numpy :::\n')

print(' \n  Ejercicios 1 \n ')
arreglo=np.zeros(10)
arreglo[4]=1
print(arreglo)

print('\n Ejercicios 2 \n ')
arreglo=np.random.randint(10,49,10 )
arreglo2=np.linspace(10,49,10)
arreglo3=np.arange(10,50,4) 
print(arreglo)
print(arreglo2)
print(arreglo3)

print('\n Ejercicios 3 \n  ')

print(arreglo[::-1])
print(arreglo2[::-1])
print(arreglo3[::-1])

print('\n Ejercicios 4 \n')
a4=np.random.random(size=(10,10))

zmin,zmax=a4.min(),a4.max()

print('El valor mínimo es: ',zmin)
print('El valor máximo es: ',zmax)

print('\n Ejercicios 5 \n')
a5=np.linspace(0,1,12)
print('\n',a5)

print('\n Ejercicios 6 \n')
