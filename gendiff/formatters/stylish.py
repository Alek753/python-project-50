import itertools
REPLACER = ' '


def make_string(current_data, depth):
    if not isinstance(current_data, dict):
        if isinstance(current_data, bool):
            return str(current_data).lower()
        if current_data is None:
            return 'null'
        return str(current_data)
    current_indent = REPLACER * (depth * 4)
    out_data = []
    for key, value in current_data.items():
        out_data.append(f'{current_indent}{key}: {make_string(value, depth + 1)}')
    return '\n'.join(itertools.chain("{", out_data, [REPLACER * (depth - 1) * 4 + "}"]))


def form_data(indent, data, key, depth):
    return f"{indent}{data['key']}: " \
           f"{make_string(data[key], depth + 1)}"


def inner(data, depth=1):
    if not isinstance(data, dict):
        return str(data)
    deep_indent = REPLACER * (depth * 4 - 2)
    indent = REPLACER * (depth - 1) * 4
    lines = []

#    print('deep_indent_size', deep_indent_size)

    for value in data.values():
        if value['operation'] == 'unchanged':
            lines.append(form_data(f"{deep_indent}  ", value, 'value', depth))

#            lines.append(f"{deep_indent}  {value['key']}: {value['value']}")

            continue
        if value['operation'] == 'changed':

#            lines.append(f"{deep_indent}- {value['key']}: {value['prev']}")
#            lines.append(f"{deep_indent}+ {value['key']}: {value['new']}")

            lines.append(form_data(f"{deep_indent}- ", value, 'prev', depth))
            lines.append(form_data(f"{deep_indent}+ ", value, 'new', depth))
            continue
        if value['operation'] == 'added':
#            lines.append(f"{deep_indent}+ {value['key']}: {value['value']}")
            lines.append(form_data(f"{deep_indent}+ ", value, 'value', depth))
            continue
        if value['operation'] == 'removed':
#            lines.append(f"{deep_indent}- {value['key']}: {value['value']}")
            lines.append(form_data(f"{deep_indent}- ", value, 'value', depth))
            continue
        if value['operation'] == 'nested':
            lines.append(f"{deep_indent}  {value['key']}: "
                         f"{inner(value['value'], depth + 1)}")
            continue
    result = itertools.chain("{", lines, [indent + "}"])
    return "\n".join(result)


def make_stylish(diff):
    return inner(diff, 1)
