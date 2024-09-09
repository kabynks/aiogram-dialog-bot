import pandas as pd
from catboost import CatBoostRegressor


def predict(features:pd.DataFrame)-> pd.DataFrame:
    model = CatBoostRegressor()
    model.load_model("best_model")
    res = model.predict(features)
    df = pd.DataFrame({'predict':res})
    return df