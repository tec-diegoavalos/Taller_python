# -*- coding: utf-8 -*-
"""
Created on Tue May 25 11:18:36 2021

@author: L01268185
"""

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

x=np.linspace(1,10,10)
y=np.random.randint(1,10,10)
print(x)
 

plt.plot(xpoints, ypoints,'r^')
plt.plot(x, y,'b')
plt.show()


