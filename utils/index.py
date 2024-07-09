import tensorflow as tf
import keras
from sklearn.preprocessing import MinMaxScaler
from utils import resources,index
import numpy as np

# model = resources.lstm_migas

scaler = MinMaxScaler(feature_range=(0,1))

def predict(model,data, num_prediction,lag):
    prediction_list = data.iloc[-lag:].values
    
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