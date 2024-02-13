import json
import yaml


def read_data(file_path):
    ext = file_path.split('.')[-1]
    with open(file_path, 'r') as file_in:
        return parse(file_in.read(), ext)


def parse(data, ext):
    if ext == 'json':
        return json.loads(data)
    elif ext == 'yml' or ext == '.yaml':
        return yaml.safe_load(data)
    else:
        raise ValueError('Unsupported file format')
