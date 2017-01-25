# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 17:10:33 2017

@author: stpl
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 13:40:30 2017

@author: stpl
"""
from matplotlib import pyplot
import mysql.connector as sql
import numpy as np

#datbase operations for fetching data.....
db = sql.connect(user  = 'root', password = 'root', host = '172.20.2.41', port = '3306', database = 'Payworld_Analytics');
cur = db.cursor();

cur.execute("select mrp, day(Transaction_Date) as day from Payworld_Analytics.MLY_2016_10  where Retailercode = '1515445' and mrp > 0");
data_11 = cur.fetchall();
cur.close();

data_11.append('black');
print(data_11);

for i in  range(len(data_11)-2):
    pyplot.scatter(np.array(data_11[i][1], dtype = np.float64), np.array(data_11[i][0], dtype = np.float64), color = data_11[len(data_11)-1]);

        
pyplot.scatter(None, None, color = data_11[len(data_11)-1], label = '11-2016');

pyplot.legend();
        
pyplot.xlabel("Days");
pyplot.ylabel("Sales");
pyplot.title("Sales data of Retailer : 1515455 on 11-2016");
pyplot.grid(True, lw = 1, ls = '-', c = 'green');

pyplot.show();

