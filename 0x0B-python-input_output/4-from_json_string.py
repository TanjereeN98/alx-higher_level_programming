#!/usr/bin/python3
"""from_json_string function"""


def from_json_string(my_str):
    """convert string to obj"""
    import json
    return json.loads(my_str)
