#!/usr/bin/python3
"""
determines if dataset uses utf-8 encoding
"""


def validUTF8(data):
    """
    determines wheteher input data
    list which is a list of integers
    is a valid utf-8 dataset
    """

    num_bytes = 0

    for byte in data:
        if num_bytes == 0:
            if byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            elif byte >> 7 != 0:
                return False
        else:
            if byte >> 6 != 0b10:
                return False

            num_bytes -= 1

            if num_bytes < 0:
                return False

    return num_bytes == 0
