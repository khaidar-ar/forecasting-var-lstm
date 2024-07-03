import streamlit as st
import pandas as pd
import requests
import json
# import pickle as pk
import numpy as np
# import sklearn
from sklearn.preprocessing import MinMaxScaler
import utils.resources as resources
import joblib as jb
import keras as kr
# from keras.models import load_model # type: ignore



model = kr.saving.load_model(resources.lstm_migas)



# scaler = MinMaxScaler(feature_range=(0,1))
# df_migas = scaler.fit_transform(data.iloc[:,:1])
# df_migas.shape(1)


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
        
# data_mg = df_migas.values
# data_mg = df_train_scaled[:,:1]
# look_back = 12
# import tensorflow as tf  # Import TensorFlow
# def predict(num_prediction, model,lag):
    prediction_list = df_migas[-lag:]
    
    for _ in range(num_prediction):
        x = prediction_list[-lag:]
        x = x.reshape((1, lag, 1))
        # x = np.reshape((x, (x.shape[0], x.shape[1], 1)))
        x = tf.convert_to_tensor(x, dtype=tf.float64)
        out = model.predict(x)
        prediction_list = np.append(prediction_list, out)
    prediction_list = prediction_list[lag-1:]
    prediction_list = prediction_list.reshape((-1))
    return prediction_list
    
# def predict_dates(num_prediction):
    last_date = df['Date'].values[-1]
    prediction_dates = pd.date_range(last_date, periods=num_prediction+1).tolist()
    return prediction_dates

# num_prediction = 10
# forecast = predict(num_prediction, loaded_model)
# forecast_dates = predict_dates(num_prediction)
# ft_migas_scale= sc.inverse_transform(forecast.reshape(-1, 1))
# abs(ft_migas_scale)
# abs(forecast)
