import uvicorn
from fastapi import FastAPI,Request
import numpy as np
import pickle
import sklearn


app = FastAPI()



model = pickle.load(open("flight_rf.pkl", "rb"))




@app.post("/predict")
async def predict(uploadForm:dict):
    data = uploadForm['data']
    new_data = list(data.values())
    return model.predict([new_data])[0]
 




if __name__ == "__main__":
    uvicorn.run(app, host = '0.0.0.0', port = 8501)