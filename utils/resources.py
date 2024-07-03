import resource
import pandas as pd

data_bps = 'C:/z-priority/project/python/forecasting/resource/data-bps-ekspor-migas-non-migas-93-23.xlsx'
lstm_migas = 'C:/z-priority/project/python/forecasting/model/model_migas'
# lstm_migas = 'C:/z-priority/project/python/forecasting/model/lstm_migas_model.h5'
lstm_non_migas = ''
var_model = 'C:/z-priority/project/python/forecasting/model/var.joblib'

# model_migas = jb.load(migas_model_lstm,'r')
#/lstm_migas_model = jb.load(migas_model_lstm,'r')
def init():
    
    data =  pd.read_excel(data_bps,parse_dates=['Date'], index_col='Date')

    # remove comma and blank space
    data = data.replace(r'\s+', '', regex=True)
    data = data.replace(r',', '.', regex=True)
    # convert string column to float
    data=data.iloc[:,0:3].astype('float')
    return data