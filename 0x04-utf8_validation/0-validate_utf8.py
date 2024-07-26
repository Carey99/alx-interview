#!/usr/bin/python3
"""
    A method that determines if a given data set
    represents a valid UTF-8 encoding.
    prototype: def validUTF8(data)
    Return: True if data is a valid UTF-8 encoding, else return False
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data,
    therefore you only need to handle the 8 least
    significant bits of each integer
"""


def validUTF8(data):
    """
        A method that determines if a given data set
        represents a valid UTF-8 encoding.
    """
    bytes = 0
    for byte in data:
        byte = byte & 255
        if bytes:
            if byte >> 6 != 2:
                return False
            bytes -= 1
            continue
        while (1 << abs(7 - bytes)) & byte:
            bytes += 1
        if bytes == 1 or bytes > 4:
            return False
        bytes = max(bytes - 1, 0)
    return bytes == 0
