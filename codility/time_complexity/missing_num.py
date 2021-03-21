#!/bin/python3

"""
An array A consisting of N different integers is given. The array contains
integers in the range [1..(N + 1)], which means that exactly one element is
missing.

Your goal is to find that missing element.
"""


def missing_num(A):
    n = len(A) + 1
    val = n * (n + 1) // 2
    arr_sum = sum(A)

    return val - arr_sum

# Example execution:
# (1, 3, 2, 5) --> 4