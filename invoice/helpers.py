

def sanitize_form_data(data_dict):
    new_dict = {}
    # Convert values to single values if they are lists with one item
    for key, value in data_dict.items():
        if isinstance(value, list) and len(value) == 1:
            new_dict[key] = value[0]

    return new_dict
