#!/usr/bin/python3
"""
Module to calculate the perimeter of an islan1d
in grid represents land mass of 1 by 1 while 0 represents
a water mass
"""


def island_perimeter(grid):
    """
    calculates the perimeter of an
    island represented by a grid
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # find perimeter if cell is land
            if grid[i][j] == 1:
                perimeter += 4
                # if not on the edge andneighbouring cells
                # are land, decrement perimeter
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
