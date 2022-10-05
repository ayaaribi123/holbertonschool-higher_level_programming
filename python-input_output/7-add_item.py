#!/usr/bin/python3
"""add argument and save them in a file"""

import sys
if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__(
        '6-load_from_json_file').load_from_json_file

    filename = "add_item.json"

    try:
        new = load_from_json_file(filename)
    except FileNotFoundError:
        new = []

"""add argument and save them in a file"""
save_to_json_file(new + sys.argv[1:], filename)
