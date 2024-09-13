"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.14
"""
from typing import Dict, Tuple
import logging
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

def split_data(data: pd.DataFrame, parameters: Dict) -> Tuple:
    X = data[parameters['features']].drop(columns='PRICE')
    print("Column", X.columns)
    y = data['PRICE']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=parameters['test_size'], random_state=parameters['random_state']
    )
    return X_train, X_test, y_train, y_test


def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> RandomForestRegressor:
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    return model

def evaluate_model(regressor: RandomForestRegressor, X_test: pd.DataFrame, y_test: pd.Series):
    y_pred = regressor.predict(X_test)
    logger = logging.getLogger(__name__)
    score = r2_score(y_test, y_pred)
    logger.info("The model has a coefficient R^2 of %.3f on test data.", score)
    return score