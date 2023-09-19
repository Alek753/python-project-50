import json
import yaml


def parsing(file_path):
    ext = file_path[-6:]
    with open(file_path, 'r') as file_in:
        if ext.find('.json') > 0:
            return json.load(file_in)
        elif ext.find('.yml') > 0 or ext.find('.yaml') > 0:
            return yaml.safe_load(file_in)
