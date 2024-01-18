import json


def make_diff(data1, data2):
    all_keys = sorted(data1.keys() | data2.keys())
    same_keys = (data1.keys() & data2.keys())
    removed = (data1.keys() - data2.keys())
    added = (data2.keys() - data1.keys())
    result = {}
    for key in all_keys:
        description = {'key': key}
        if key in removed:
            description['operation'] = 'removed'
            description['value'] = data1[key]
        elif key in added:
            description['operation'] = 'added'
            description['value'] = data2[key]
        elif key in same_keys and data1[key] == data2[key]:
            description['operation'] = 'unchanged'
            description['value'] = data1[key]
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            description['operation'] = 'nested'
            description['value'] = make_diff(data1[key], data2[key])
        else:
            description['operation'] = 'changed'
            description['prev'] = data1[key]
            description['new'] = data2[key]
        result[key] = description
    return result
#    return json.dumps(result, indent=2, separators=('', ': ')).replace('"', '')
