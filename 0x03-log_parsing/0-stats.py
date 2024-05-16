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
    sorted_keys = sorted(status.keys())
    for key in sorted_keys:
        print(f"{key}: {status[key]}")


if __name__ == "__main__":
    import sys
    import re

    status_count = {}
    total_file_size = 0
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                printStats(status_count, total_file_size)
                count = 1
            else:
                count += 1
            line = line.split()
            try:
                file_size = line[-1]
                total_file_size += int(file_size)
            except (IndexError, ValueError):
                pass
            try:
                status = line[-2]
                if status in ["200", "301", "400", "401", "403",
                              "404", "405", "500"]:
                    if status in status_count.keys():
                        status_count[status] += 1
                    else:
                        status_count[status] = 1
            except IndexError:
                pass

        printStats(status_count, total_file_size)
    except KeyboardInterrupt:
        printStats(status_count, total_file_size)
        raise