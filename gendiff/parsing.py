import json
import yaml


def parsing(file_path):
    with open(file_path, 'r') as file_in:
        if file_path[-6:].find('.json') > 0:
            return json.load(file_in)
        elif file_path[-6:].find('.yml') > 0:
            return yaml.safe_load(file_in)
