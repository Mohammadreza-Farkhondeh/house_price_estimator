import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
from sklearn import linear_model


df = pd.read_csv('price-estimator/your_updated_file_name.csv')

cdf = df[['Room','Parking','Warehouse','Elevator','Area_Price','AvgPrice']]

#We divide the data into two categories
msk = np.random.rand(len(df)) < 0.95
train = cdf[msk]
test = cdf[~msk]

#from sklearn import linear_model
regr = linear_model.LinearRegression()
train_x = np.asanyarray(train[['Room','Parking','Warehouse','Elevator','AvgPrice']])
train_y = np.asanyarray(train[['Area_Price']])
regr.fit (train_x, train_y)

#prediction
Room = 0
Parking = 0
Warehouse =0
Elevator = 0
AvgPrice=3.5e+09

y_hat= regr.predict([[Room,Parking,Warehouse,Elevator,3.585754e+09]])
print(round(y_hat[0][0] / 1000000, 5))
