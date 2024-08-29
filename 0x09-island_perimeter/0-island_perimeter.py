#!/usr/bin/python3
"""
    returns a perimeter of an island described in grid
    grid - list of list of int
    0 represents water
    1 represents land
    each cel is a square, with a side length of 1
    cells are connected horizontally/vertically not diagonally
    grid is rectangular with its width and height not exceeding 100
    Grid is completely sorrounded by water
"""


def island_perimeter(grid):
    count = 0
    for lst in grid:
        for i in lst:
            if lst[i] == 1:
                count += 1
    length = (count + 1) // 2
    perimeter = 2 * (length + length)
    return perimeter
