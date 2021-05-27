# -*- coding: utf-8 -*-
"""
Created on Tue May 25 13:38:33 2021

@author: L01268185
"""

import pandas as pd
import matplotlib.pyplot as plt

archivo='fortunas.xlsx'

info=pd.read_excel(archivo)

#Subtabla con algunas columas
valores =info[['Nombre','Fortuna',]]

ax=valores.plot.bar(x='Nombre',y='Fortuna', rot=-90, color='darkgray')
plt.show()

print(valores)

