import joblib as jb
import pandas as pd
import keras

data_bps = 'C:/z-priority/project/python/forecasting/resource/data-bps-ekspor-migas-non-migas-93-23.xlsx'
migas = 'C:/z-priority/project/python/forecasting/model/model_migas'
non_migas = 'C:/z-priority/project/python/forecasting/model/model_non_migas'
var_path = 'C:/z-priority/project/python/forecasting/model/var.joblib'

lstm_migas = keras.models.load_model(migas)
lstm_non_migas = keras.models.load_model(non_migas)
model_var= jb.load(var_path,'r')


def init():
    
    data =  pd.read_excel(data_bps,parse_dates=['Date'], index_col='Date')

    # remove comma and blank space
    data = data.replace(r'\s+', '', regex=True)
    data = data.replace(r',', '.', regex=True)
    # convert string column to float
    data=data.iloc[:,0:3].astype('float')
    return data

def init_date(model,range,migas=False,non_migas=False,both=False):
    date = pd.date_range(start='1/1/2024', periods=range,freq='MS')
    result = pd.DataFrame({
        'Date' : date
    })
    if(migas):
        result.loc[:,'Migas'] = list(model)
    if(non_migas):
        result.loc[:,'Non Migas'] = list(model)
    return result

def init_multiple(model1,model2,range):
    date = pd.date_range(start='1/1/2024', periods=range,freq='MS')
    result = pd.DataFrame({
        'Date' : date
    })
    result.loc[:,'Migas'] = list(model1[1:])
    result.loc[:,'Non Migas'] = list(model2[1:])
    return result