#!/usr/bin/python3
""" define function that print the name """


def say_my_name(first_name, last_name=""):
    """
    function that print full first and last name

    Args:
        first_name
        last_name
    Raises:
        TypeError: if the first name or the last name are not string
    Returns:
        first and last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
