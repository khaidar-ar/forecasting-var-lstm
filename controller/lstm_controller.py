from fastapi import FastAPI,HTTPException
import uvicorn
app = FastAPI()


@app.post('/LSTM')
async def predict(range : int , migas : bool , nonmigas : bool):
    result = list()
    result.append(range)
    if(migas):
        result.append("modelMigas")
    if(nonmigas):
        result.append("modelNonmigas")
    return {"result":result}