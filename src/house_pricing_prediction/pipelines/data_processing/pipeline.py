"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import preprocess_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=preprocess_data,
            inputs="housing_data",
            outputs="preprocessed_housing_data",
            name="preprocessed_housing_data_node"
        )
    ])
