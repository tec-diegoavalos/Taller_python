# -*- coding: utf-8 -*-
"""
Created on Tue May 25 11:40:16 2021

@author: L01268185
"""

import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 2)
plt.grid(color='red',linestyle='--',linewidth=0.2)
plt.plot(x,y)
plt.title("SALES")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 1 )
plt.grid(color='green',linestyle='--',linewidth=0.2)
plt.plot(x,y)
plt.title("INCOME")

plt.suptitle("MY SHOP")
plt.show()
