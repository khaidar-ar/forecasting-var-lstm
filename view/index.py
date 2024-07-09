import streamlit as st
import pandas as pd
import requests
import json
from utils import resources,index
from service import lstm_service,var_service
import tensorflow as tf
import pydantic
import resource

tf.compat.v1.reset_default_graph()




API_LSTM = "http://127.0.0.1:8080/LSTM"
API_VAR = "http://127.0.0.1:8080/VAR"




# with content :
def main(activated):
    if activated :
        st.write("""
            # The value of Indonesia's oil & gas and non-oil & gas exports
            """
        )
        filename = resources.data_bps
        # path = "C:/z-priority/project/python/forecasting/resource/data-bps-ekspor-migas-non-migas-93-23.xlsx"
        df = resources.init()

            # convert string column to float
        df.iloc[:,0:3]=df.iloc[:,0:3].astype('float')
        st.write("## Oil & Gas Graph Monthly Since 1993")
        st.line_chart(df.iloc[:,:1])
        st.write("## Non-oil & Gas Graph Monthly Since 1993")
        st.line_chart(df.iloc[:,1:])
        

def setFeature(opt1,opt2,opt3) :
    selected = st.selectbox(
        "Select feature to forecast",
        (opt1,opt2,opt3)
    )
    return selected
    

def setRange(years):
    range = st.slider(
        "Determine the forecasting period",0,years,1
    )
    st.write("Forecasting for ",range," years")
    return range

def selection(feature,p_migas,p_nonmigas,p_both):       
    migas = False
    nonmigas = False
    all = False
    if(feature == p_migas):
        migas = True
    if(feature == p_nonmigas):
        nonmigas = True
    if(feature == p_both):
        all = True
    return migas,nonmigas,all

def var_page(title,feature,range,result):
    st.title(title)   
    feature
    range
    result
    

 
def lstm_page():
    migas = "Oil & Gas"
    nonMigas = "Non-oil & Gas"
    both = "All"
    st.title("""
            Forecasting Oil & Gas and Non-Oil & Gas Value of Indonesia's Using LSTM
            """)
    f = setFeature(migas,nonMigas,both)
    range = setRange(100)
    if st.button("Predict"):
        p_migas,p_nonmigas,p_both = selection(f,migas,nonMigas,both)
        payload = {"range":range,"migas":p_migas,"nonmigas":p_nonmigas,"all":p_both}
        try:
            # predict = index.predict(resources.lstm_migas,resources.init().iloc[:,:1],num_prediction=range,lag=12)
            # st.table(lstm_service.generate_lstm(range,both=True))
            st.write('api')
            response = requests.post(API_LSTM,params=payload)
            result = pd.read_json(response.json())
            st.table(result)
        except requests.exceptions.RequestException as e:
            st.error(f"Error occurred while making the request: {e}")


def var_page():
    migas = "Oil & Gas"
    nonMigas = "Non-oil & Gas"
    both = "All"
    st.title("""
            VAR Forecasting Oil & Gas and Non-Oil & Gas Value of Indonesia's Using LSTM
            """)
    f = setFeature(migas,nonMigas,both)
    range = setRange(100)
    if st.button("Predict"):
        p_migas,p_nonmigas,p_both = selection(f,migas,nonMigas,both)
        payload = {"range":range,"migas":p_migas,"nonmigas":p_nonmigas,"all":p_both}
        try:
            # st.table(var_service.generate_var(range,migas=True))
            st.write('api')
            response = requests.post(API_VAR,params=payload)
            response.raise_for_status()
            result = pd.read_json(response.json())
            st.table(result)
        except requests.exceptions.RequestException as e:
            st.error(f"Error occurred while making the request: {e}")