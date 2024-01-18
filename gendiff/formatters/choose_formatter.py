from gendiff.formatters.stylish import make_stylish


def choose_formatter(diff, formatter):
    if formatter == 'stylish':
        return make_stylish(diff)
