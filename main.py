from timeit import timeit

import pandas as pd
from fastapi import FastAPI
from joblib import load
from sklearn.pipeline import Pipeline

from constants import model_path
from patient_dto import Patient

model: Pipeline = load(model_path)
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/predict")
async def predict(patient: Patient):
    df = pd.DataFrame([patient.dict()])
    class_probabilities = model.predict_proba(df)[0]
    heart_disease_proba = class_probabilities[1]
    return {"prob": heart_disease_proba}
