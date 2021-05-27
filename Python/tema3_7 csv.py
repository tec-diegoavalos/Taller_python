# -*- coding: utf-8 -*-
"""
Created on Tue May 25 14:17:29 2021

@author: L01268185
"""

import pandas as pd
import matplotlib.pyplot as plt

Data=pd.read_csv('fortunas.csv',usecols=['Nombre', 'Pais', 'Fortuna', 'Edad', 'Empresa'])
print(Data)

valores =Data[['Nombre','Fortuna',]]
print(valores)

ax=valores.plot.bar(x='Nombre',y='Fortuna', rot=75, color='gray')
plt.show()

