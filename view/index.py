import streamlit as st
import pandas as pd
import requests
import json
# import controller.lstm_controller
from utils import path
from service import lstm_service


API_URL = "http://127.0.0.1:8080/LSTM"
migas = "Oil & Gas"
nonMigas = "Non-oil & Gas"



# with content :
def main(activated):
    if activated :
        st.write("""
            # The value of Indonesia's oil & gas and non-oil & gas exports
            """
        )
        filaname = path.data_bps
        # path = "C:/z-priority/project/python/forecasting/resource/data-bps-ekspor-migas-non-migas-93-23.xlsx"
        df = pd.read_excel(filaname,parse_dates=['Date'], index_col='Date')
        df = df.drop(df.iloc[:,0:1],axis=1)
            # remove comma and blank space
        df = df.replace(r'\s+', '', regex=True)
        df = df.replace(r',', '.', regex=True)

            # convert string column to float
        df.iloc[:,0:3]=df.iloc[:,0:3].astype('float')
        st.write("## Oil & Gas Graph Monthly Since 1993")
        st.line_chart(df.iloc[:,:1])

        st.write("## Non-oil & Gas Graph Monthly Since 1993")
        st.line_chart(df.iloc[:,1:])
        st.write(lstm_service.test())
        

def setFeature(opt1,opt2) :
    selected = st.selectbox(
        "Select feature to forecast",
        (opt1,opt2)
    )
    return selected
    

def setRange(years):
    range = st.slider(
        "Determine the forecasting period",0,years,1
    )
    st.write("Forecasting for ",range," years")
    return range

def selection(feature,p_migas,p_nonmigas):       
    migas = False
    nonmigas = False
    if(feature == p_migas):
        migas = True
    if(feature == p_nonmigas):
        nonmigas = True
    return migas,nonmigas

def var_page(title,feature,range,result):
    st.title(title)   
    feature
    range
    result
    
    
 
def lstm_page():
    st.title("""
            Forecasting Oil & Gas and Non-Oil & Gas Value of Indonesia's Using LSTM
            """)
    f = setFeature(migas,nonMigas)
    range = setRange(100)
    if st.button("Predict"):
        p_migas,p_nonmigas = selection(f,migas,nonMigas)
        payload = {"range":range,"migas":p_migas,"nonmigas":p_nonmigas}
        try:
            response = requests.post(API_URL,params=payload)
            # response.raise_for_status()
            res = response.json()
            st.write(json.dumps(res))
            print(res)
            print(range)
                
        except requests.exceptions.RequestException as e:
            st.error(f"Error occurred while making the request: {e}")


