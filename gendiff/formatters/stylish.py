import itertools

def make_stylish(diff):
    def inner(data, depth=0):
#        print(diff)
        if not isinstance(data, dict):
            return str(data)
        deep_indent_size = depth + 1
        deep_indent = ' ' * deep_indent_size
        indent = ' ' * depth
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
                lines.append(f"{deep_indent * 2}  {value['key']}: "
                             f"{inner(value['value'], deep_indent_size)}")
                continue
        result = itertools.chain("{", lines, [indent + "}"])
        return '\n'.join(result)
    return inner(diff, 1)
