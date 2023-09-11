import json


def generate_diff(file1, file2):
    print(file1)
    data1 = json.load(open(file1))
    data2 = json.load(open(file2))
    all_keys = sorted(data1.keys() | data2.keys())
    same_keys = sorted(data1.keys() & data2.keys())
    minus = sorted(data1.keys() - data2.keys())
    plus = sorted(data2.keys() - data1.keys())
    result = {}
    for key in all_keys:
        if key in same_keys:
            result.update({f'   {key}':data1[key]})
        elif key in minus:
            result.update({f' - {key}':data1[key]})
        elif key in plus:
            result.update({f' - {key}':data2[key]})
    print(data1)
    print(data2)
    print(result)
    out_file = open('gendiff/out.txt', 'w')
    print(json.dumps(result, sort_keys=True, indent=4))
#    file1.close()
#    file2.close()
    out_file.close()