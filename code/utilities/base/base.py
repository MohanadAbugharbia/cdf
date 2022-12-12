from pydantic import BaseModel
from typing import Type

def parseModel(model_class: type[BaseModel], json_data: dict) -> BaseModel:
    # Use the `parse_obj` class method of the model class to parse the JSON data
    model = model_class.parse_obj(json_data)
    return model
