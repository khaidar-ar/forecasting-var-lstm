import joblib as jb
import utils.resources as resources

model = jb.load(resources.var_model,'r')
data = resources.init()
data = data.iloc[:,:][:3].values
def var_forecast_result(end,lag):
    # load model
    # result = model.predict 
    # set range
    # model append with date
    # return result in dataframe
    end *=12
    result = model.predict(params=data,lags=lag,start=1,end=end)
    return result