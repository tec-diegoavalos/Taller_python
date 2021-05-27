# -*- coding: utf-8 -*-
"""
Created on Tue May 25 11:33:18 2021

@author: L01268185
"""
import matplotlib.pyplot as plt
import numpy as np
'''
x=[1,3,5,7]
y=[2,4,6,8]

plt.plot(x,y,'o--r')
'''
x=np.array([80,85,90,95,100,105,110,115,120,125])
y=np.array([240,250,260,270,280,290,300,310,320,330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x,y,'o:b')
plt.grid(color='green',linestyle='--',linewidth=0.2)
plt.show()
