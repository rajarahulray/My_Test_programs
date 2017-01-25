# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 10:17:15 2016

@author: stpl
"""

import statistics as s
from matplotlib import style, pyplot
import numpy as np
import random

style.use('fivethirtyeight');

x = np.array([1,2,3,4,5,6], dtype = np.float64);
y = np.array([5,4,6,5,6,7], dtype = np.float64);

def create_random_data(how_many, variance, step = 2, co_relation = False):
    val = 1;
    ys = [];
    for i in range(how_many):
        y = val + random.randrange(-variance, variance); 
        ys.append(y);
        if co_relation and co_relation == 'pos':
            val += step;
        elif co_relation and co_relation == 'neg':
            val -= step;
    xs = [i for i in range(len(ys))];
    return np.array(xs, dtype = np.float64), np.array(ys, dtype = np.float64);
    
def bestfit_slope_and_intercept(x,y):
    m = ( 
         ((s.mean(x) * s.mean(y)) - s.mean(x*y)) /
         ((s.mean(x) * s.mean(x) - s.mean(x*x)))
    );
    b = s.mean(y) - m * s.mean(x);
    return m, b;
    
def squared_error(y_orig, y_line):
    return sum ((y_line - y_orig)**2);
    
def r_square(y_orig, y_line):
    y_mean_line = [s.mean(y_orig) for y in y_orig];
    squared_error_regr = squared_error(y_orig, y_line);
    squared_error_y_mean = squared_error(y_orig, y_mean_line);
    return 1-(squared_error_regr / squared_error_y_mean);
                   
#x,y = create_random_data(40, 6, 2, co_relation = False);

m, b = bestfit_slope_and_intercept(x, y);

regression_line = [(m * X + b) for X in x ];
predict_x = 12;
predict_y = (m * predict_x) + b;
print('prediction_plot ({},{})'.format(predict_x,predict_y)); 

r_squared = r_square(y, regression_line);
print('r ** 2 value: ',r_squared);

print("Prediction {}".format(regression_line));
      
pyplot.scatter(x,y);
pyplot.scatter(predict_x, predict_y, color = 'r');
pyplot.plot(x,regression_line);

pyplot.show();
