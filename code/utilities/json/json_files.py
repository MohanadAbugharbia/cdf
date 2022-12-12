import json
import os

def import_json_file(file: str) -> dict | list:
    if os.stat(file).st_size == 0:
        return {}
    with open(file, "r") as file_object:
        file_json = json.load(file_object)
    return file_json

def export_json_file(file: str, json_object: dict | list, indent: int = 4) -> None:
    with open(file, "w") as file_object:
        json.dump(json_object, file_object, indent=indent)