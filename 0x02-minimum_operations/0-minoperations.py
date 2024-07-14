#!/usr/bin/python3
"""
    There a single character H in a text file.
    text editor can only execute two operations: copy all and paste
    given n, write a method to calculate the fewest number of operation
    needed to result into exactly n H characters
"""


def minOperations(n: int) -> int:
    if n <= 1:
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(n // i) + i
    return n
