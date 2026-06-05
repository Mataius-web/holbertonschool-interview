#!/usr/bin/python3
"""Module that seeks how many turns it takes to reach n just with
Copy and past"""


def minOperations(n):
    """Function that does it"""
    if n <= 1:
        return 0

    turns = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            turns += factor
            n = n / factor
        factor += 1
    return turns
