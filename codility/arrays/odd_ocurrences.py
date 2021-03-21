#!/bin/python3

"""
A non-empty array A consisting of N integers is given. The array contains an
odd number of elements, and each element of the array can be paired with
another element that has the same value, except for one element that is left
unpaired.
"""

from collections import defaultdict

def unpaired(A):
    appearances = defaultdict(int)

    for num in A:
        appearances[num] += 1
        if appearances[num] == 2:
            appearances.pop(num)

    return list(appearances.keys())[0]
