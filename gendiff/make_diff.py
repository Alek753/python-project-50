import json


def make_diff(data1, data2):
    all_keys = sorted(data1.keys() | data2.keys())
    same_keys = sorted(data1.keys() & data2.keys())
    minus = sorted(data1.keys() - data2.keys())
    plus = sorted(data2.keys() - data1.keys())
    result = {}
    print('all_keys', all_keys)
    print('same_keys', same_keys)
    print('minus', minus)
    print('plus', plus)
    for key in all_keys:
        if key in same_keys:
            if data1[key] == data2[key]:
                result.update({f'  {key}': data1[key]})
            elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
                print(data1[key])
                print(data2[key])
                result.update({f'  {key}': make_diff(data1[key], data2[key])})
            else:
                result.update({f'- {key}': data1[key]})
                result.update({f'+ {key}': data2[key]})
        elif key in minus:
            result.update({f'- {key}': data1[key]})
        elif key in plus:
            result.update({f'+ {key}': data2[key]})
    return json.dumps(result, indent=2, separators=('', ': ')).replace('"', '')
