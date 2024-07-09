import streamlit as st
import pandas as pd
import requests
import json
import numpy as np
import tensorflow as tf
from utils import resources,index
import joblib as jb
import keras
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'


model_migas = resources.lstm_migas
model_non_migas = resources.lstm_non_migas
model = ''


def generate_lstm(numb,migas=False,non_migas=False,both=False):
    data = resources.init()
    append_date =''
    range = numb*12
    if(migas):
        data = data.iloc[:,:1]
        model = model_migas
        result = index.predict(model,data,range-1,12)
        append_date = resources.init_date(result,range,migas,non_migas,both)
    if(non_migas):
        data = data.iloc[:,1:]
        model = model_non_migas
        result = index.predict(model_non_migas,data,range-1,12)
        append_date = resources.init_date(result,range,migas,non_migas,both)
    if(both):
        data_migas = data.iloc[:,:1]
        data_non_migas = data.iloc[:,1:]
        model_migasv = model_migas
        model_nonmigas = model_non_migas
        result_migas = index.predict(model_migasv,data_migas,range,12)
        result_non_migas= index.predict(model_nonmigas,data_non_migas,range,12)
        append_date = resources.init_multiple(result_migas,result_non_migas,range)
    return append_date