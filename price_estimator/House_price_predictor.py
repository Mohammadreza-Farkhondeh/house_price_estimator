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
def predict_price (Room, parking ,Warehouse,Elevator,AvgPrice):
    y_hat= regr.predict([[Room,parking,Warehouse,Elevator,AvgPrice]])
    return(round(y_hat[0][0] / 1000000, 5))

    