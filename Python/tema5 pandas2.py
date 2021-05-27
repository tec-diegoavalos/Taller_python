# -*- coding: utf-8 -*-
"""
Created on Tue May 25 21:06:59 2021

@author: L01268185
"""

import pandas as pd
import numpy as np

df = pd.DataFrame(np.array([[1, 2], [4, 5], [7, 8]]))

print('DataFrame:')
print(df)

print('Valores de la primera fila del DataFrame:')
print(df.loc[0])

print('Valores de la primera fila del DataFrame:')
print(df.iloc[0,:])


print('\n Muestra los últimos 5 registros \n')
print(df.tail())

print('\n Muestra los primeros 5 registros \n')
print(df.head())

print('\n Estadistica Básica')
print(df.describe())

print('\n Información Básica de tabla')
print(df.info())

print("Tamaño de tabla")
print(df.shape)

print("Número de registro")
print(len(df.index))

print("Número de registro")
print(df.mean())

print("Número de Count")
print(df.count())

