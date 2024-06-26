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
        mask = 1 << 7
        if num_bytes == 0:
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (byte >> 6 == 0b10):
                return False
        num_bytes -= 1
    return num_bytes == 0
