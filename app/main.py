from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import nltk
import pickle
import json
import os
import logging
import sys, errno
import traceback

app = FastAPI()
# relative to current working directory
if not os.path.isfile("models/model.pkl"):
    logging.info("models/model.pkl does not exist. Downloading with dvc.")
    os.system("dvc get -v -o models/ https://github.com/itsderek23/covid19-repo-recommender models/model.pkl")

try:
    model = pickle.load(open("models/model.pkl","rb"))
except:
    logging.error("Unable to load model.")
    logging.error(traceback.format_exc())
    sys.exit(errno.EINTR)

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
