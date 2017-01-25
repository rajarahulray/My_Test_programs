import pandas as pd
import quandl as q
#You have exceeded the anonymous user limit of 50 calls per day. To make more calls today, please register for a free Quandl account and then include your API key with your requests.
import math
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

df = q.get('WIKI/GOOGL');
df = df[['Adj. Open', 'Adj. High','Adj. Low','Adj. Close','Adj. Volume',]];

df['HL%'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0

df['%change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HL%', '%change','Adj. Volume']]

forecast = 'Adj. Close';
df.fillna(-99999, inplace = True);
forecast_out = int(math.ceil(0.01*len(df)));

df['Label'] = df[forecast].shift(forecast_out);
df.dropna(inplace = True);

x = np.array(df.drop(['Label'], 1));
y = np.array(df['Label']);

x = preprocessing.scale(x);
y = np.array(df['Label']);

x_train, x_test, y_train, y_test = cross_validation.train_test_split(x, y, test_size = 0.2);
print(x_train, y_train);
clf = LinearRegression();
clf.fit(x_train, y_train);

print(clf.fit(x_train, y_train))
accuracy = clf.score(x_test, y_test);

print('Acuuracy: {}%'.foramt(accuracy));