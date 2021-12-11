import os.path

import pandas as pd
from fastapi import FastAPI, Response
from joblib import load
from sklearn.pipeline import Pipeline
from starlette import status

from constants import model_path
from health_check import health_check
from patient_dto import Patient

model: Pipeline = load(model_path)
app = FastAPI()


@app.get("/")
async def root():
    return "Hi"


@app.post("/predict")
async def predict(patient: Patient):
    df = pd.DataFrame([patient.dict()])
    class_probabilities = model.predict_proba(df)[0]
    heart_disease_proba = class_probabilities[1]
    return {"prob": heart_disease_proba}


@app.get("/health", status_code=200)
async def health(response: Response):
    health_check_response = health_check()
    if health_check_response.get("status", "pass") == "fail":
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    return health_check_response
