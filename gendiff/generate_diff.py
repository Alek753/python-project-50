import json


def generate_diff(file1, file2):
    print(file1)
    in_file1 = open(file1, "r")
    in_file2 = open(file2, "r")
    data1 = json.load(in_file1)
    data2 = json.load(in_file2)
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
    in_file1.close()
    in_file2.close()
    return json.dumps(result, indent=2, separators=('', ': ')).replace('"', '')
