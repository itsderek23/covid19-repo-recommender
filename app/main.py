from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import nltk
import pickle
import json

app = FastAPI()
# relative to current working directory
model = pickle.load(open("models/model.pkl","rb"))

# pd.DataFrame([["Python", "Data"]]).to_json(orient="split")
# {"columns":[0,1],"index":[0],"data":[["Python","Data"]]}
class PredictPayload(BaseModel):
    columns: list
    data: list
    # https://fastapi.tiangolo.com/tutorial/schema-extra-example/
    class Config:
        schema_extra = {
            "example": {
                "columns": [0,1],
                "data": [["Python","Data"]],
            }
        }

@app.post("/predict")
async def _predict(payload: PredictPayload):
    input = pd.read_json(payload.json(), orient='split')
    output = model.predict(None,input)
    return output
