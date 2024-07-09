from fastapi import FastAPI,HTTPException
import uvicorn
import pandas as pd
# from utils.resources import resources
from utils import resources
from utils import index
from service import lstm_service,var_service

app = FastAPI()


print("In module products __package__, __name__ ==", __package__, __name__)

@app.post('/LSTM')
async def predict(range : int , migas : bool , nonmigas : bool,all:bool):
    # result.append(range)
    if(migas):
        # result.append('migas')
        result = lstm_service.generate_lstm(range,migas,nonmigas)
    if(nonmigas):
        # result.append('nonmigas')
        result = lstm_service.generate_lstm(range,migas,nonmigas)
    if(all):
        result = lstm_service.generate_lstm(range,both=all)
    return result.to_json()

@app.post('/VAR')
async def predict(range : int , migas : bool , nonmigas : bool,all:bool):
    # result.append(range)
    if(migas):
        # result.append('migas')
        result = var_service.generate_var(range,migas,nonmigas)
    if(nonmigas):
        # result.append('nonmigas')
        result = lstm_service.generate_lstm(range,migas,nonmigas)
    if(all):
        result =var_service.generate_var(range,both=all)
    return result.to_json()