#!/usr/bin/python3
"""save_to_json_file"""


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation
    Args:
        my_obj (obj): object that will be stored
        filename (str): data storage
    """
    import json
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
