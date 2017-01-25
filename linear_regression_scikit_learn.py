# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 10:16:16 2017

@author: stpl
"""

#from sklearn import datasets
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np

lr = linear_model.LinearRegression()
#boston = datasets.load_boston()
#y = boston.target
x = np.array([8,9,10,11], dtype = np.float64)
y = np.array([2621,3055,3133,7020], dtype = np.float64 )
# cross_val_predict returns an array of the same size as `y` where each entry
# is a prediction obtained by cross validation:
predicted = cross_val_predict(lr, x, y, cv=4)

fig, ax = plt.subplots()
ax.scatter(y, predicted)
#ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()