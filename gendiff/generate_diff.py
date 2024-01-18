from gendiff.parsing import parsing
from gendiff.make_diff import make_diff
from gendiff.formatters.choose_formatter import choose_formatter


def generate_diff(file1, file2, formatter='stylish'):
    data1 = parsing(file1)
    print(data1)
    data2 = parsing(file2)
    print(data2)
    return choose_formatter(make_diff(data1, data2), formatter)
