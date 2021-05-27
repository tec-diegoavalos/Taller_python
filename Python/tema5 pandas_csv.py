# -*- coding: utf-8 -*-
"""
Created on Tue May 25 21:46:52 2021

@author: L01268185
"""
import pandas as pd
import numpy as np
import random as rd

def ganancias (total):
    ganancia=total*3
    return ganancia

def popularidad (fila):
    resultado=(fila['Internet']*.5)+(fila['Computadora']*.15)+(fila['Telefono']*.35)
    return resultado

df=pd.read_csv('inegi2.csv',index_col='Year',header=0)
datos=pd.DataFrame(df)
datos2=datos

print ("Visualización de la tabla original")
print(datos)

print("\n Información de la tabla ")
print(datos.info())

print("\n Estadistica de la tabla ")
print(datos.describe())

#Limpieza de la tabla
print("\n Reemplazar NaN por 0")
datos2=datos.fillna({'Internet':0,'Cable':-10})
print (datos2)

print("\n Reemplazar NR y NAN por 0")
datos2=datos2.replace('NR','0')
datos2=datos2.replace('NAN','0')

#Convertir los '0' en números
datos2['Computadora']=datos2.Computadora.astype(float)
datos2['Internet']=datos2.Internet.astype(float)
datos2['Cable']=datos2.Cable.astype(float)

print("\n Estadistica de la tabla ")
print(datos2.info())
print(datos2.describe())

#Generar nuevas columnas con la información 
datos2["Popularidad"]=datos2.apply(popularidad,axis=1)

datos2["Ganancias"]=datos["Telefono"].apply(ganancias)
print(datos2)

#Agrupación de la información
promedio=datos2.groupby('Compania').mean()
print(promedio)

#Guardar en un nuevo archivo la información
print("\n Importar la tabla procesada en un nuevo archivo ")
datos2.to_csv('salida_inegi.csv',header=True,index=True)
