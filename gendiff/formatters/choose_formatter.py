from gendiff.formatters.stylish import make_stylish
from gendiff.formatters.plain import make_plain


def choose_formatter(diff, formatter):
    if formatter == 'stylish':
        return make_stylish(diff)
    if formatter == 'plain':
        return make_plain(diff)
