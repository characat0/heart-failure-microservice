import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder
from lightgbm import LGBMClassifier
from joblib import dump
from constants import model_path

import pathlib


def generate_model():
    current_path = pathlib.Path(__file__).parent
    data_path = current_path / "data/heart.csv"
    df = pd.read_csv(data_path)
    df.columns = [x.replace('_', '') for x in df.columns]
    df.columns = [x[0].lower() + x[1:] for x in df.columns]
    X = df.drop('heartDisease', axis=1)
    y = df['heartDisease']
    # using 42 as seed to improve model performance ;)
    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.3, random_state=42)
    ohe = OneHotEncoder()
    categorical = X.select_dtypes('object').columns
    ct = make_column_transformer((ohe, categorical), remainder='passthrough')
    model = LGBMClassifier(random_state=0)
    pipe = make_pipeline(ct, model)
    pipe.fit(X_train, y_train)
    # this could fail is the pipeline is too complex
    dump(pipe, model_path)
    return model_path


if __name__ == "__main__":
    print(generate_model())
