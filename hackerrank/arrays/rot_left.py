#!/bin/python3

"""
Given an array (its values as a space separated list), perform d left
rotations taking into account that the array is circular.
"""

import copy

def rot_left(a, d):
    # Maybe better like return a[d:] + a[:d]
    orig = copy.copy(a) # shallow copy
    for i in range(len(a)):
        a[i-d] = orig[i]

    return a

if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))

    print(rot_left(a, d))
