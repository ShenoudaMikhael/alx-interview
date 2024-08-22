#!/usr/bin/python3
"""0-validate_utf8"""


def validUTF8(data):
    """validUTF8 function"""

    num_of_bytes = 0

    for value in data:
        value_binary = bin(value).replace("0b", "").rjust(8, "0")[-8:]
        if num_of_bytes == 0:
            if value_binary.startswith("110"):
                num_of_bytes = 1
            if value_binary.startswith("1110"):
                num_of_bytes = 2
            if value_binary.startswith("11110"):
                num_of_bytes = 3
            if value_binary.startswith("10"):
                return False
        else:
            if not value_binary.startswith("10"):
                return False
            num_of_bytes -= 1

    return num_of_bytes == 0
