def make_string(current_data):
    if isinstance(current_data, dict):
        return '[complex value]'
    if isinstance(current_data, bool):
        return str(current_data).lower()
    if current_data is None:
        return 'null'
    if isinstance(current_data, int):
        return current_data
    return f"'{str(current_data)}'"


def make_plain(data, node=''):
    result = []
    for key, value in data.items():
        node_name = f"{node}{value['key']}"
        property_string = f"Property '{node_name}'"
        if value['operation'] == 'removed':
            result.append(f"{property_string} was removed")
        if value['operation'] == 'added':
            result.append(f"{property_string} was added "
                          f"with value: {make_string(value['value'])}")
        if value['operation'] == 'changed':
            result.append(f"{property_string} was updated. "
                          f"From {make_string(value['prev'])} "
                          f"to {make_string(value['new'])}")
        if value['operation'] == 'nested':
            result.append(make_plain(value['value'], f"{node_name}."))
        if result == []:
            raise ValueError('Unknown operation type!')
    return '\n'.join(result)
