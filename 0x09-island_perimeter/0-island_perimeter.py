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
    if type(grid) != list:
        return 0
    n = len(grid)
    for i, row in enumerate(grid):
        m = len(row)
        for j, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == m - 1 or (m > j + 1 and row[j + 1] == 0),
                i == n - 1 or (len(grid[i + 1]) > j and grid[i + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter
