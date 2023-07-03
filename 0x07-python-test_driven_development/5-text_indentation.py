#!/usr/bin/python3
"""
Contains the definition of 'text_indentation' function.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    one_line = ""
    for letter in text:
        one_line += letter
        if letter in [".", "?", ":"]:
            print(one_line.strip())
            print()
            one_line = ""
    print(one_line.strip(), end="")
        
