#!/bin/python3

"""
Given an integer N, obtain the longest gap of its binary representation.
A binary gap is the amount of 0's surrounded by 1's, e.g. 100001001 would
have 2 binary gaps, the first one of 4 and the second one of 2.
"""

from collections import Counter


def binary_gap(N):
    binary = "{0:b}".format(N)
    longest_gap = 0
    curr_gap = 0

    start = False
    breakpoint()
    for num in binary:
        if start and num == "0":
            curr_gap += 1
        elif num == "1":
            if start and curr_gap > longest_gap:
                longest_gap = curr_gap
            start = True
            curr_gap = 0
    
    return longest_gap

print(binary_gap(1041))