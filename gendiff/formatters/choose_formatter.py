from gendiff.formatters.stylish import make_stylish
from gendiff.formatters.plain import make_plain
from gendiff.formatters.json import make_json


def choose_formatter(diff, formatter):
    if formatter == 'stylish':
        return make_stylish(diff)
    if formatter == 'plain':
        return make_plain(diff)
    if formatter == 'json':
        return make_json(diff)
