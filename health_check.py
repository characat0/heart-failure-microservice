import os

import pandas as pd
from joblib import load
from sklearn.pipeline import Pipeline

from constants import model_path


def health_check():
    status = "pass"
    notes = []
    model_exists = os.path.exists(model_path)
    if not model_exists:
        status = "fail"
        notes.append(f"model cannot be found at {model_path}")
    obj = {
        "age": 49,
        "sex": "M",
        "chestPainType": "NAP",
        "restingBP": 160,
        "cholesterol": 180,
        "fastingBS": 1,
        "restingECG": "Normal",
        "maxHR": 202,
        "exerciseAngina": "N",
        "oldpeak": 1,
        "sTSlope": "Up"
    }
    test_df = pd.DataFrame([obj])
    try:
        model: Pipeline = load(model_path)
        model.predict_proba(test_df)
    except Exception as e:
        status = "fail"
        notes.append(str(e))
    return {"status": status, "notes": notes}