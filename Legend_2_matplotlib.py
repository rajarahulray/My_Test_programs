# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 16:13:48 2017

@author: stpl
"""

import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(0, 6, 1024)
Y1 = np.sin(X)
Y2 = np.cos(X)
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(X, Y1, c = 'k', lw = 3., label = 'sin(X)')
plt.plot(X, Y2, c = '.5', lw = 3., ls = '--', label = 'cos(X)')
plt.legend()
plt.show()