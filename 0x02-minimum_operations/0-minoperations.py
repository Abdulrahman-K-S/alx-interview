#!/usr/bin/python3
"""
Task 0. Minimum Operations

Calculate the minimum operations needed to reach the solution
"""


def minOperations(n: int) -> int:
    """minOperations

    This function calculates the minimum operations needed
    to result in exactly n H characters in a file

    Arguments:
        n (int): The number of H to be present.

    Return:
        (int): The number of operations needed to reach that state.
    """
    minOp, div = 0, 2
    while n > 1:
        while n % div:
            div += 1
        minOp += div
        n = int(n / div)
    return minOp
