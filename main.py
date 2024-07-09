import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from view import index
# sidebar,content=st.columns([0.5,4])

    
    
with st.sidebar :
    selected= option_menu(
        menu_title="Menu",
        # options=["VAR","LSTM"],
        options =  ["Overview","VAR","LSTM"],
        menu_icon= "list"
    )
if selected == "Overview":
    index.main(True)
if selected == "VAR":
    index.main(False)
    index.var_page()
    
if selected == "LSTM":
    index.main(False)
    index.lstm_page()
    
