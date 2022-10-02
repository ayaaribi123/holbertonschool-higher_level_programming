#!/usr/bin/python3
"""read file"""


def read_file(filename=""):
    """read file"""
    file = open("my_file_0.txt", "r", encoding='utf-8')
    print(file.read())
