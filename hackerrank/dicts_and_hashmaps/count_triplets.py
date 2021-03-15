#!/bin/python3

"""
Given an array of integer, count the number of triplets (x, y, z) which follow
a geometric progression of a given ratio (r); e.g. for r=5, (5, 25, 125) would
be a triplet.
Triplets do not have to be consecutive, e.g. the can be in positions (0, 4, 10).
"""

from collections import defaultdict, Counter


def count_triplets(arr, r):
    appearances = Counter(arr)  # could be understood as right hand vals
    seen = defaultdict(int) # could be understood as left hand vals
    num_triplets = 0
    for val in arr:
        first_val = val // r
        second_val = val
        third_val = second_val * r
        appearances[val] -= 1
        # not second_val % r because we only want exact multiples of the ratio
        if seen[first_val] and appearances[third_val] and not second_val % r:
            num_triplets += seen[first_val] * appearances[third_val]
        seen[second_val] += 1
    
    return num_triplets


if __name__ == '__main__':
    nr = input().rstrip().split()
    n = int(nr[0])
    r = int(nr[1])
    arr = list(map(int, input().rstrip().split()))

    print(count_triplets(arr, r))
