# -*- coding: utf-8 -*-
"""
Created on Tue May 25 18:14:14 2021

@author: L01268185
"""
import pandas as pd

alumnos={'Matricula':['a011','a012','a013','a014','a015'],
         'Nombre':['Santiago', 'Lizzie','David','Elizabeth','José'],
         'Notas':['95','98','90','88','92'],
         'Deportes':['Futbol', 'Voleyvo','Basketbol','Tenis','Golf'],
         'Materias': ['Cálculo', 'Matemáticas','Física','Programación','Literatura']}

print (alumnos)
df=pd.DataFrame(alumnos)

print (df)
