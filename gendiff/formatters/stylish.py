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
        out_data.append(f'{current_indent}{key}: '
                        f'{make_string(value, depth + 1)}')
    return '\n'.join(itertools.chain("{", out_data,
                     [REPLACER * (depth - 1) * 4 + "}"]))


def form_data(indent, data, key, depth):
    return f"{indent}{data['key']}: " \
           f"{make_string(data[key], depth + 1)}"


def make_stylish(data, depth=1):
    deep_indent = REPLACER * (depth * 4 - 2)
    lines = []
    for value in data.values():
        if value['operation'] == 'unchanged':
            lines.append(form_data(f"{deep_indent}  ", value, 'value', depth))
            continue
        if value['operation'] == 'changed':
            lines.append(form_data(f"{deep_indent}- ", value, 'prev', depth))
            lines.append(form_data(f"{deep_indent}+ ", value, 'new', depth))
            continue
        if value['operation'] == 'added':
            lines.append(form_data(f"{deep_indent}+ ", value, 'value', depth))
            continue
        if value['operation'] == 'removed':
            lines.append(form_data(f"{deep_indent}- ", value, 'value', depth))
            continue
        if value['operation'] == 'nested':
            lines.append(f"{deep_indent}  {value['key']}: "
                         f"{make_stylish(value['value'], depth + 1)}")
            continue
        if lines == []:
            raise ValueError('Unknown operation type!')
    result = itertools.chain("{", lines, [REPLACER * (depth - 1) * 4 + "}"])
    return "\n".join(result)
