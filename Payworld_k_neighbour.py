# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn import cross_validation, neighbors
from matplotlib import pyplot

data_frame = pd.read_csv('D:\Payworld_Analytics_MLY_12-2016_retailer_mrp_3.5_to_30000.csv');
data_frame.drop(['Retailercode'], 1, inplace = True);
data_frame.drop(['Retailername'], 1, inplace = True);

train= np.array(data_frame.drop(['mrp'],1));
test = np.array(data_frame['mrp']);
                
x_train, x_test, y_train, y_test = cross_validation.train_test_split(train, test, test_size = 0.4);

clf = neighbors.KNeighborsClassifier()
clf.fit(x_train, y_train);

accuracy = clf.score(x_test, y_test);
print('Accuracy: {}'.format(accuracy));

#Predicting Test Data
pre_data = np.array([[432,90],[985,412],[12,22.3]]);
pre_data = pre_data.reshape(len(pre_data),-1);
prediction = clf.predict(pre_data);

#Prediction....
print(prediction);
#print(type(data_frame['abs(mrp)']));     
#data_frame['abs(mrp)'].plot();
#pyplot.scatter(pre_data[0],pre_data[1] , color = 'red');