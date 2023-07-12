#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    return the minimum number of operations required to get exactly
    n H characters in a file
    """
    if n <= 1:
        return 0
    for operation in range(2, n+1):
        if n % operation == 0:
            return minOperations(int(n/operation)) + operation
