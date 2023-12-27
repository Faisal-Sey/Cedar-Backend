

def sanitize_form_data(data_dict):
    new_dict = {}
    # Convert values to single values if they are lists with one item
    for key, value in data_dict.items():
        if key[-2:] == '[]' and len(value) == 1:
            new_dict[key[:-2]] = value
        elif isinstance(value, list) and len(value) == 1:
            new_dict[key] = value[0]
        elif isinstance(value, list) and len(value) > 1:
            new_dict[key[:-2]] = value

    return new_dict
