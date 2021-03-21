#!/bin/python3

"""
A non-empty array A consisting of N integers is given. The consecutive
elements of array A represent consecutive cars on a road. Array A contains
only 0s and/or 1s:
- 0 represents a car traveling east,
- 1 represents a car traveling west.

The goal is to count passing cars. We say that a pair of cars (P, Q), where
0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling
to the west.
"""

def crossings(A):
    west = [0] * len(A)

    curr_west = 0
    for idx in range(len(A)-1, -1, -1):
        if A[idx] == 1:
            curr_west += 1
        west[idx] = curr_west
    
    crossings = 0
    for idx, car in enumerate(A):
        if car == 0:
            crossings += west[idx]

    return crossings if crossings <= 1000000000 else -1

# Example execution
# [0, 0] --> 0
# [1, 1] --> 0
# [0, 1, 1, 1] --> 3
# [1, 1, 1, 0] --> 0
# [0, 1, 0, 1, 1] --> 5