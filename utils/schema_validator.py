import json

from jsonschema import validate


def validate_schema(response_json, schema_file):

    with open(schema_file) as file:
        schema = json.load(file)


    validate(
        instance=response_json,
        schema=schema
    )