# -*- coding: utf-8 -*-
"""
Created on Tue May 25 12:39:07 2021

@author: L01268185
"""

import matplotlib.pyplot as plt
import numpy as np

dias=['Lunes','Martes','Miercoles','Jueves','Viernes']
hombres=[20,34,30,35,27]
mujeres=[25,32,34,20,25]

#Obtenemos la posición de cada día 0,1,2..
x=np.arange(len(dias))

#Definimos el ancho de cada barra
width=0.4

fig, ax=plt.subplots()

#Gener las barras para hombres y mujeres
rectah=ax.bar(x - width/2, hombres, width,label='Hombres')
rectam=ax.bar(x + width/2, mujeres, width,label='Mujeres')

#Añadir las etiquetas al gráfico
ax.set_title('Reporte de Asistencia hombres y mujeres')
ax.set_ylabel('Asistencia')
ax.set_xlabel('Días')

#Añadir etiqueta a cada día
ax.set_xticks(x) #Orden
ax.set_xtickslabels(dias)

#Añadir la leyenda
ax.legend()

plt.show()

