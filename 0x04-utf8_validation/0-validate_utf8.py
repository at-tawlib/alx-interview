#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding
    returns true if it is else false
    """
    count = 0
    for num in data:
        # If the count is 0, check how many leading 1's
        # there are in the current integer
        if count == 0:
            if (num >> 5) == 0b110:
                count = 1
            elif (num >> 4) == 0b1110:
                count = 2
            elif (num >> 3) == 0b11110:
                count = 3
            elif (num >> 7) != 0:
                return False
        # else check if the current integer is a continuation byte
        else:
            if (num >> 6) != 0b10:
                return False
            count -= 1

    # If the count is still not 0 after iterating
    # through all the integers, it is invalid
    return count == 0
