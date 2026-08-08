import json


def load_test_data(filename):

    path = f"test_data/{filename}"

    with open(path) as file:
        return json.load(file)