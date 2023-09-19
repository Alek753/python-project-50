import json
from gendiff.parsing import parsing


def generate_diff(file1, file2):
    data1 = parsing(file1)
#    print(data1)
    data2 = parsing(file2)
#    print(data2)
    all_keys = sorted(data1.keys() | data2.keys())
    same_keys = sorted(data1.keys() & data2.keys())
    minus = sorted(data1.keys() - data2.keys())
    plus = sorted(data2.keys() - data1.keys())
    result = {}
    for key in all_keys:
        if key in same_keys:
            if data1[key] == data2[key]:
                result.update({f'  {key}': data1[key]})
            else:
                result.update({f'- {key}': data1[key]})
                result.update({f'+ {key}': data2[key]})
        elif key in minus:
            result.update({f'- {key}': data1[key]})
        elif key in plus:
            result.update({f'+ {key}': data2[key]})
    return json.dumps(result, indent=2, separators=('', ': ')).replace('"', '')
