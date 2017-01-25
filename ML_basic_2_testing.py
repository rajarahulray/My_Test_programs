# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 10:17:15 2016

@author: stpl
"""

import statistics as s
from matplotlib import pyplot, style
import numpy as np

style.use('dark_background');

x = np.array([1,2,3,4,5,6,7,8], dtype = np.float64);
y = np.array([2,4,3,6,3,2,5,2], dtype = np.float64);

def bestfit_slope_and_intercept(x,y):
    m = (((s.mean(x) * s.mean(y)) - (s.mean(x*y)) / (s.mean(x)**2 - s.mean(x**2))));
    b = s.mean(y) - m * s.mean(x);
    return m, b;
    
def squared_error(y_orig, y_line):
    return sum ((y_line - y_orig));
    
def r_square(y_orig, y_line):
    y_mean_line = [s.mean(y) for y in y_orig];
    squared_error_regr = squared_error(y_orig, y_line);
    squared_error_y_mean = squared_error(y_orig, y_mean_line);
    return 1-(squared_error_regr - squared_error_y_mean);
                   

m, b = bestfit_slope_and_intercept(x, y);

regression_line = [(m * X + b) for X in x ];
predict_x = 15;
predict_y = (m * predict_x) + b;

r_squared_value = r_square(y, regression_line);
print(r_squared_value);

pyplot.scatter(x,y);
pyplot.scatter(predict_x, predict_y, color = 'r');
pyplot.plot(x,regression_line);
pyplot.show();
