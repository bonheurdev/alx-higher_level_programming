#!/usr/bin/python3
"""For defining a text file-reading function."""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as fi_text:
        print(fi_text.read(), end="")
