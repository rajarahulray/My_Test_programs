# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 16:51:50 2017

@author: stpl
"""

import matplotlib.pyplot as plt
N = 16
for i in range(N):
 plt.gca().add_line(plt.Line2D((0, i), (N - i, 0), color = '.75'))
plt.grid(True)
plt.axis('scaled')
plt.show()