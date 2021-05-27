# -*- coding: utf-8 -*-
"""
Created on Tue May 25 13:00:16 2021

@author: L01268185
"""

import matplotlib.pyplot as plt
import numpy as np

x1=np.linspace(0.0, 5.0)
y1=np.cos(2 * np.pi*x1) * np.exp(-x1)

x2=np.linspace(0.0, 2.0)
y2=np.cos(2 * np.pi*x2)

fig, (ax1,ax2)=plt.subplots(2,1)
fig.suptitle('Oscilaciones')

ax1.plot(x1,y1,'o-')
ax1.set_ylabel('O. Amortiguada')

ax2.plot(x2,y2,'.-')
ax2.set_xlabel('time (s)')
ax2.set_ylabel('O. Sin Amortiguada')

plt.show()