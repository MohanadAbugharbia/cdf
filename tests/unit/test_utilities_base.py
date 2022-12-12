import pytest
from pydantic import ValidationError, BaseModel
from code.utilities import parseModel

class Model(BaseModel):
    name: str
    age: int
    is_active: bool


def test_parseModel():
    # Test data
    json_data = {
        'name': 'John Doe',
        'age': 30,
        'is_active': True
    }
    # Parse the JSON data using the parseModel function
    model = parseModel(Model, json_data)

    # Assert that the parsed model object has the same attributes and values as the JSON data
    assert model.name == json_data['name']
    assert model.age == json_data['age']
    assert model.is_active == json_data['is_active']

def test_parseModel_invalid_data():
    json_data = {
        "name": "John Doe"
    }
    with pytest.raises(ValidationError):
        parseModel(Model, json_data)
