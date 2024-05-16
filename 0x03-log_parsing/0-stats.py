#!/usr/bin/python3
"""
Task 0. Log parsing

A script that reads stdin line by line and computes metrics.
"""

import sys


def printStats(file_size, status):
    """printStats

    This function takes the total file size and the
    statues that were called and prints them.

    Arguments:
        file_size (int): The total file size to be printed.
        status (dict{int, int}): A dictionary of the statues that were called.
    """
    print("File size: {}".format(file_size))
    for key, value in sorted(status.items()):
        if value != 0:
            print("{}: {}".format(key, value))


total_file_size = 0
count = 0
possible_status = {200: 0, 301: 0, 400: 0, 401: 0,
                   403: 0, 404: 0, 405: 0, 500: 0}
try:
    for line in sys.stdin:
        args = line.split()

        status_code = int(args[-2])
        file_size = int(args[-1])

        if status_code in possible_status:
            possible_status[status_code] += 1

        total_file_size += file_size
        count += 1

        if count == 10:
            printStats(total_file_size, possible_status)
            count = 0
    printStats(total_file_size, possible_status)
except KeyboardInterrupt:
    raise
finally:
    printStats(total_file_size, possible_status)
