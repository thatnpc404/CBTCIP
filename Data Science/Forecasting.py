from statsmodels.tsa.arima_model import ARIMA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from sklearn.model_selection import train_test_split
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm
import pmdarima as pm


def alcohol():
    df=pd.read_csv('Alcohol_Sales.csv',encoding='utf-8')
    x=df['S4248SM144NCEN']
    x_train,x_test=train_test_split(x,shuffle=False,random_state=42,test_size=0.01)


    #ad=adfuller(x)[1]
    #adfuller p value > 0.05 , so we differentiate to make it stationary
    #plot_pacf(x.diff().dropna())  computing p value
    #plot_acf(x.diff().dropna())   computing q value
    #plt.show()

    sorder=(2, 1, 2, 12)
    model=sm.tsa.statespace.SARIMAX(x_train,order=(4, 0, 0),sorder=(2, 1, 2, 12))
    fit_=model.fit()
    predicted=fit_.forecast(steps=len(x_test))
    mse=mean_squared_error(x_test,predicted)
    rmse=mean_squared_error(x_test,predicted,squared=False)
    print('Seasonal model :','MSE : ',mse,"\t",'RMSE : ',rmse)

def miles():
    df=pd.read_csv('Miles_Traveled.csv',encoding='utf-8')
    print(df.columns)
    x=df['TRFVOLUSM227NFWA']
    x_train,x_test=train_test_split(x,shuffle=False,random_state=42,test_size=0.01)
    sorder=(2, 1, 2, 12)
    model=sm.tsa.statespace.SARIMAX(x_train,order=(4, 0, 0),sorder=(2, 1, 2, 12))
    fit_=model.fit()
    predicted=fit_.forecast(steps=len(x_test))
    mse=mean_squared_error(x_test,predicted)
    rmse=mean_squared_error(x_test,predicted,squared=False)
    print('Seasonal model :','MSE : ',mse,"\t",'RMSE : ',rmse)


print("Miles traveled")
miles()
print("Alcohol Sales")
alcohol()





