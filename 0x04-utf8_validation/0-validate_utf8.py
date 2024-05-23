#!/usr/bin/python3
"""
Task 0. UTF-8 Validation

Determines whether a given data is a valid UTF-8 or not.
"""


def validUTF8(data):
    """validUTF8

    A method that determines if a given data set
    represents a valid UTF-8 encoding or not.

    Arguments:
        data (List[int]): A list of integers that represent characters to
                          check their UTF-8.

    Return:
        (bool): [True: If data is a valid UTF-8 / False: If data is not
                 a valid UTF-8]
    """
    n_bytes = 0
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        byte = num & 0xFF

        if n_bytes > 0:
            # Not in form '10xxxxxx'
            if not (byte & mask1 and not (byte & mask2)):
                return False
            n_bytes -= 1
        else:
            # 1-byte character (0xxxxxxx)
            if (byte & mask1) == 0:
                continue
            # Invalid scenario, as it cannot start with 10xxxxxx
            elif (byte & (mask1 | mask2)) == mask1:
                return False
            # 2-byte character (110xxxxx)
            elif (byte & (mask1 | mask2 | (1 << 5))) == (mask1 | mask2):
                n_bytes = 1
            # 3-byte character (1110xxxx)
            elif (byte & (mask1 | mask2 | (1 << 5) | (1 << 4))
                  ) == (mask1 | mask2 | (1 << 5)):
                n_bytes = 2
            # 4-byte character (11110xxx)
            elif (byte & (mask1 | mask2 | (1 << 5) | (1 << 4) | (1 << 3))
                  ) == (mask1 | mask2 | (1 << 5) | (1 << 4)):
                n_bytes = 3
            else:
                return False
    return n_bytes == 0
