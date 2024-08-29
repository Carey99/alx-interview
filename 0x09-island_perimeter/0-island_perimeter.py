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
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4

                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2

                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2
    return perimeter
