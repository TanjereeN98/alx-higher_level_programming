#!/usr/bin/python3


def text_indentation(text):
    """a function that prints a text with 2 new lines
      after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_str = text.strip().replace('. ', '.\n\n') \
        .replace('? ', '?\n\n').replace(': ', ':\n\n')
    print(new_str, end='')
