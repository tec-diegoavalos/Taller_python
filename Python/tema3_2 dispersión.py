# -*- coding: utf-8 -*-
"""
Created on Tue May 25 12:24:22 2021

@author: L01268185
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap='rainbow')
plt.colorbar()
plt.show()
