"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.14
"""
import pandas as pd
import logging
import numpy as np

def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    
    numerical_features = [
        'BEDS',
        'BATH',
        'PROPERTYSQFT',
        'PRICE',
        'LATITUDE',
        'LONGITUDE'
    ]

    categorical_features = [
        'BROKERTITLE',
        'TYPE',
        'ADDRESS',
        'STATE',
        'MAIN_ADDRESS',
        'ADMINISTRATIVE_AREA_LEVEL_2',
        'LOCALITY',
        'SUBLOCALITY',
        'STREET_NAME',
        'LONG_NAME',
        'FORMATTED_ADDRESS',
    ]

    # Handle missing values by filling with median for numerical and "Unknown" for categorical
    for col in categorical_features:
        data[col].fillna("Unknown", inplace=True)

    for col in numerical_features:
        data[col].fillna(data[col].mean(), inplace=True)

    # Handle missing values by filling with mean for numerical and "Unknown" for categorical 
    data['BEDS'].fillna(data['BEDS'].mean(), inplace=True) 
    data['BATH'].fillna(data['BATH'].mean(), inplace=True) 
    data['PROPERTYSQFT'].fillna(data['PROPERTYSQFT'].mean(), inplace=True) # 
    
    # Apply log transformation to skewed features (if distribution is highly skewed) 
    data['PRICE'] = np.log1p(data['PRICE']) 
    data['PROPERTYSQFT'] = np.log1p(data['PROPERTYSQFT']) # Return preprocessed data return data

    data = pd.get_dummies(data, drop_first=True)

    return data

