#!/bin/python3

"""
Given three integers A, B and K, returns the number of integers within the
range [A..B] that are divisible by K.
"""

import math

def count_div(A, B, K):
    if A == B == 0:
        return 1
    elif A == B and B > K:
        return 1 if not B % K else 0
    elif B < K:
        return 0

    return math.floor(B/K) - math.floor((A - 1)/K)

# Example execution

# [1, 10, 2] --> 5
# [3, 9, 3] --> 3
# [3, 8, 3] --> 2
