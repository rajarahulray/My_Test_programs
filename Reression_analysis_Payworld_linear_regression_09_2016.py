# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 13:40:30 2017

@author: stpl
"""
from matplotlib import pyplot ,style
import mysql.connector as sql
import numpy as np
import statistics as s

style.use('fivethirtyeight');

   
def bestfit_slope_and_intercept(x,y):
    m = ( 
         ((s.mean(x) * s.mean(y)) - s.mean(x*y)) /
         ((s.mean(x) * s.mean(x) - s.mean(x*x)))
    );
    b = s.mean(y) - m * s.mean(x);
    return m, b;
    
def squared_error(y_orig, y_line):
    return sum ((y_line - y_orig));
    
def r_square(y_orig, y_line):
    y_mean_line = [s.mean(y_orig) for y in y_orig];
    squared_error_regr = squared_error(y_orig, y_line);
    squared_error_y_mean = squared_error(y_orig, y_mean_line);
    return 1-(squared_error_regr - squared_error_y_mean);

#datbase operations for fetching data.....
db = sql.connect(user  = 'root', password = 'root', host = '172.20.2.41', port = '3306', database = 'Payworld_Analytics');
cur = db.cursor();

cur.execute("select mrp, day(Transaction_Date) as day from Payworld_Analytics.MLY_2016_9  where Retailercode = '1515445' and mrp > 0");
data_09 = cur.fetchall();
cur.close();

data_09.append('red');
#print(data_09);
x = [];
y = [];
for i in  range(len(data_09)-1):
    x.append(data_09[i][1]);
    y.append(data_09[i][0])

print(x, y);
    
x = np.array(x, dtype = np.float64);
y = np.array(y, dtype = np.float64);

m, b = bestfit_slope_and_intercept(x, y);
print('m = {} and b = {}'.format(m,b));

regression_line = [(m * xs + b) for xs in x ];
predict_x = x[len(y)-1];
predict_y = (m * predict_x) + b;
print('prediction_plot ({},{})'.format(predict_x,predict_y)); 
                        
r_squared = r_square(y, regression_line);
print('r ** 2 value: ',r_squared);



        
#pyplot.scatter(None, None, color = data_09[len(data_09)-1] );


pyplot.scatter(x, y, color = data_09[len(data_09)-1],label = '09-2016');        
pyplot.xlabel("Days");
pyplot.ylabel("Sales");
pyplot.title("Sales data of Retailer : 1515455 on 09-2016");
pyplot.grid(True, lw = 1, ls = '-', c = '0.77');
pyplot.scatter(predict_x, predict_y, color = 'b', s = 100);
pyplot.plot(x,regression_line);

pyplot.legend();
pyplot.show();

