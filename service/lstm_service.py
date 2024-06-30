import streamlit as st
import pandas as pd
import requests
import json
import pickle as pk
import numpy as np
import sklearn
from sklearn.preprocessing import MinMaxScaler
# from utility import path
import utils.path as path


migas_model_lstm = path.lstm_migas
data_bps_ekspor = path.data_bps
model_migas = pk.load(open(migas_model_lstm,'rb'))

data =  pd.read_excel(data_bps_ekspor,parse_dates=['Date'], index_col='Date')

# remove comma and blank space
data = data.replace(r'\s+', '', regex=True)
data = data.replace(r',', '.', regex=True)
# convert string column to float
data.iloc[:,0:3]=data.iloc[:,0:3].astype('float')


scaler = MinMaxScaler(feature_range=(0,1))
df_migas = scaler.fit_transform(data)
df_migas.shape(1)

def test():
    df_migas

def generate(range,selection,feature,url,predict):
    st.title("""
            Forecasting Oil & Gas and Non-Oil & Gas Value of Indonesia's Using LSTM
            """)
    f = feature
    p_range = range
    if predict:
        p_migas,p_nonmigas = selection
        payload = {"range":p_range,"migas":p_migas,"nonmigas":p_nonmigas}
        try:
            response = requests.post(url,params=payload)
            response.raise_for_status()
            return response.json()             
        except requests.exceptions.RequestException as e:
            return (f"Error occurred while making the request: {e}")
        
# data_mg = df.iloc[:,:1].values
data_mg = df_train_scaled[:,:1]
look_back = 12
# import tensorflow as tf  # Import TensorFlow
def predict(num_prediction, model):
    prediction_list = data_mg[-look_back:]
    
    for _ in range(num_prediction):
        x = prediction_list[-look_back:]
        x = x.reshape((1, look_back, 1))
        # x = np.reshape((x, (x.shape[0], x.shape[1], 1)))
        x = tf.convert_to_tensor(x, dtype=tf.float64)
        out = modelMigas.predict(x)
        prediction_list = np.append(prediction_list, out)
    prediction_list = prediction_list[look_back-1:]
    prediction_list = prediction_list.reshape((-1))
    return prediction_list
    
def predict_dates(num_prediction):
    last_date = df['Date'].values[-1]
    prediction_dates = pd.date_range(last_date, periods=num_prediction+1).tolist()
    return prediction_dates

# num_prediction = 10
# forecast = predict(num_prediction, loaded_model)
# forecast_dates = predict_dates(num_prediction)
# ft_migas_scale= sc.inverse_transform(forecast.reshape(-1, 1))
# abs(ft_migas_scale)
# abs(forecast)
