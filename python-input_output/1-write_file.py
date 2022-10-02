#!/usr/bin/python3
"""write a string to a text file"""


def write_file(filename="", text=""):
    """write a string to a text file"""
    with open(filename, "w", encoding='utf-8') as filename:
        filename.write(text)
        return len(text)
