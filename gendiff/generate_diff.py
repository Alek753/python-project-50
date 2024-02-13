from gendiff.parser import read_data
from gendiff.make_diff import make_diff
from gendiff.formatters.choose_formatter import choose_formatter


def generate_diff(file1, file2, formatter='stylish'):
    data1 = read_data(file1)
    data2 = read_data(file2)
    print(data1)
    print(data2)
    if data1 is None:
        raise ValueError(f'File {file1} is empty!')
    if data2 is None:
        raise ValueError(f'File {file2} is empty!')
    return choose_formatter(make_diff(data1, data2), formatter)
