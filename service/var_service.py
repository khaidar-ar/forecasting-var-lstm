import joblib as jb
import utils.resources as resources

model = resources.model_var
data = resources.init()
data = data.iloc[:,:][:3].values
def var_forecast_result(end):
    end *=12
    result = model.predict(params=data,lags=1,start=1,end=end)
    return result

def generate_var(num,migas=False,non_migas=False,both=False):
    append_date =''
    range = num * 12
    if(migas):
        result = var_forecast_result(num)[:,:1]
        append_date = resources.init_date(result,range,migas,non_migas)
    if(non_migas):
        result = var_forecast_result(num)[:,1:]
        append_date = resources.init_date(result,range,migas,non_migas)
    if(both):
        result1 = var_forecast_result(num)[:,:1]
        result2 = var_forecast_result(num)[:,1:]
        append_date = resources.init_multiple(result1,result2,range-1)
    return append_date