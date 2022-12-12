import json
import os
import tempfile
import pytest
from code.utilities import import_json_file, export_json_file


def test_import_json_file():
    # Create a temporary JSON file with some test data
    test_data = {"foo": 1, "bar": 2}
    _, temp_file = tempfile.mkstemp()
    with open(temp_file, "w") as f:
        json.dump(test_data, f)

    # Import the JSON data from the temporary file
    result = import_json_file(temp_file)

    # Verify that the data was correctly imported
    assert result == test_data

    # Clean up the temporary file
    os.remove(temp_file)

def test_import_json_file_file_not_found():
    # Check that the function raises a FileNotFoundError if the file does not exist
    with pytest.raises(FileNotFoundError):
        import_json_file("does-not-exist.json")

def test_import_json_file_invalid_json():
    # Create a temporary file with invalid JSON data
    _, temp_file = tempfile.mkstemp()
    with open(temp_file, "w") as f:
        f.write("this is not valid JSON")

    # Check that the function raises a JSONDecodeError if the file contains invalid JSON data
    with pytest.raises(json.JSONDecodeError):
        import_json_file(temp_file)

    # Clean up the temporary file
    os.remove(temp_file)

def test_import_json_file_empty_file():
    # Create a temporary empty file
    _, temp_file = tempfile.mkstemp()

    # Check that the function returns an empty dictionary if the file is empty
    result = import_json_file(temp_file)
    assert result == {}

    # Clean up the temporary file
    os.remove(temp_file)


def test_export_json_file():
    # Create a temporary file to export the JSON data to
    _, temp_file = tempfile.mkstemp()

    # Export some test data to the temporary file
    test_data = {"foo": 1, "bar": 2}
    export_json_file(temp_file, test_data)

    # Check that the file was created and that it contains the expected data
    assert os.path.exists(temp_file)
    with open(temp_file, "r") as f:
        exported_data = json.load(f)
    assert exported_data == test_data

    # Clean up the temporary file
    os.remove(temp_file)

def test_export_json_file_overwrite():
    # Create a temporary file with some initial data
    _, temp_file = tempfile.mkstemp()
    with open(temp_file, "w") as f:
        json.dump({"foo": 1, "bar": 2}, f)

    # Export some different test data to the temporary file
    test_data = {"baz": 3, "qux": 4}
    export_json_file(temp_file, test_data)

    # Check that the file was created and that it contains the expected data
    assert os.path.exists(temp_file)
    with open(temp_file, "r") as f:
        exported_data = json.load(f)
    assert exported_data == test_data

    # Clean up the temporary file
    os.remove(temp_file)

def test_export_json_file_indent():
    # Create a temporary file to export the JSON data to
    _, temp_file = tempfile.mkstemp()

    # Export some test data to the temporary file with a specific indent level
    test_data = {"foo": 1, "bar": 2}
    indent = 4
    export_json_file(temp_file, test_data, indent)

    # Check that the file was created and that it contains the expected data
    assert os.path.exists(temp_file)
    with open(temp_file, "r") as f:
        exported_data = json.load(f)
    assert exported_data == test_data

    # Check that the file was formatted using the specified indent level
    with open(temp_file, "r") as f:
        exported_string = f.read()
    assert "\n" + " " * indent in exported_string

    # Clean up the temporary file
    os.remove(temp_file)

def test_export_json_file_dict_and_list():
    # Create a temporary file to export the JSON data to
    _, temp_file = tempfile.mkstemp()

    # Export a dict object to the temporary file
    test_data_dict = {"foo": 1, "bar": 2}
    export_json_file(temp_file, test_data_dict)

    # Check that the file was created and that it contains the expected data
    assert os.path.exists(temp_file)
    with open(temp_file, "r") as f:
        exported_data_dict = json.load(f)
    assert exported_data_dict == test_data_dict

    # Export a list object to the temporary file
    test_data_list = [1, 2, 3, 4]
    export_json_file(temp_file, test_data_list)

    # Check that the file was created and that it contains the expected data
    assert os.path.exists(temp_file)
    with open(temp_file, "r") as f:
        exported_data_list = json.load(f)
    assert exported_data_list == test_data_list

    # Clean up the temporary file
    os.remove(temp_file)
