import json


def generate_diff(file1, file2):
    print(file1)
    data1 = json.load(open(file1))
    data2 = json.load(open(file2))
    print(data1)
    print(data2)
