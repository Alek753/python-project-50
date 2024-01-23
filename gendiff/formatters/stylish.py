import itertools
REPLACER = ' '


def inner(data, depth=0):
    if not isinstance(data, dict):
        return str(data)
    deep_indent_size = depth + 1
    deep_indent = REPLACER * deep_indent_size * 2
    indent = REPLACER * depth
    lines = []
    print('deep_indent_size', deep_indent_size)
    for value in data.values():
        if value['operation'] == 'unchanged':
            lines.append(f"{deep_indent}  {value['key']}: {value['value']}")
            continue
        if value['operation'] == 'changed':
            lines.append(f"{deep_indent}- {value['key']}: {value['prev']}")
            lines.append(f"{deep_indent}+ {value['key']}: {value['new']}")
        if value['operation'] == 'added':
            lines.append(f"{deep_indent}+ {value['key']}: {value['value']}")
            continue
        if value['operation'] == 'removed':
            lines.append(f"{deep_indent}- {value['key']}: {value['value']}")
            continue
        if value['operation'] == 'nested':
            lines.append(f"{deep_indent}  {value['key']}: "
                         f"{inner(value['value'], deep_indent_size + 1)}")
            continue
    result = itertools.chain("{", lines, [indent * depth + "}"])
    return "\n".join(result)


def make_stylish(diff):
    return inner(diff, 0)
