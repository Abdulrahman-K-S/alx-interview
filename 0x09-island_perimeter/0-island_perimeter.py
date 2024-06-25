#!/usr/bin/python3
"""
0-islan_perimeter

A function that returns the perimeter of the island described in grid.
"""


def island_perimeter(grid):
    """island_perimeter

    This method takes a list of integers lists and that represents a grid
    of water and land. Which then calculates the perimeter of the land
    and returns that number

    Arguments:
        grid (2D List): A list of integers where 0 represents water &
                        1 represents land.

    Return:
        (int): The perimeter of the grid passed to the function.
    """
    total_perimeter = 0

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == 0:
                continue

            # Up
            if r == 0 or grid[r-1][c] == 0:
                total_perimeter += 1

            # Down
            if r == len(grid) - 1 or grid[r+1][c] == 0:
                total_perimeter += 1

            # Left
            if c == 0 or grid[r][c-1] == 0:
                total_perimeter += 1

            # Right
            if c == len(row) - 1 or grid[r][c+1] == 0:
                total_perimeter += 1

    return total_perimeter
