# -*- coding: utf-8 -*-
"""
Created on Tue May 25 10:49:24 2021

@author: L01268185
"""

print(' ::: Tipos de datos ::: ')
x = str(3.5)  #x es’3.5'
y = int(3)    # y es 3
z = float(3)  # z es 3.0
print(x,y,z)


print ('\n ::: Trabajo con variables  ::: ')
x,y,z = 'Naranja', 'Piña', 'Melón'
print(x,y,z)

frutas = ['Naranja', 'Piña', 'Melón']
x, y, z = frutas
print(x,y,z)
print(frutas)


print ('\n ::: Ciclos  ::: ')
x = range(6)
for i in x:
    print(i,end=', ')

print()
    
for x in 'banana':
    print(x) #imprime carácter por carácter

txt = "¡Las mejores cosas de la vida son gratis!"
print('gratis' in txt)


txt = " ¡Las mejores cosas de la vida son gratis! "
if 'gratis' in txt:
    print('Si, ‘gratis’ está incluido.')

x=2
x **= 3

print("\n ::: Cambiar partes de una lista ::: ")

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

print("\n ::: Cambiar valores de lista ::: ")
thislist=["apple","banana","cherry"]
print(thislist)
thislist[1:3] = ['orange','pineapple']
print(thislist)



