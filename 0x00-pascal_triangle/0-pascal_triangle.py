#!/usr/bin/python3
""" 0-pascal_triangle.py

This module is aimed to solve the pascal triangle problem.
"""


def binomial_coefficient(n, k):
    """Binomial Coefficient

    Arguements:
        n (int): The row to be calculated.
        k (int): The column to be calculated.

    Return:
        (int): The number yeilded by nCm
    """
    if k == 0 or k == n:
        return 1
    else:
        return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)

def pascal_triangle(n):
    """Pascal Triangle

    Arguments:
        n (int): The height of the pascal triangle to be returned

    Return:
        (list): The flattened pascal triangle of height n
    """
    if type(n) is not int:
        raise TypeError("n must be an integer")
    elif n <= 0:
        return []

    pTriangle = []
    for row in range(n):
        rowlist = []
        for col in range(row + 1):
            if col == 0 or col == row:
                rowlist.append(1)
            else:
                rowlist.append(binomial_coefficient(row, col))
        pTriangle.append(rowlist)

    return pTriangle
