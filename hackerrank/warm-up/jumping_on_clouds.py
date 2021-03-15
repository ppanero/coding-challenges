#!/bin/python3

"""
Input a length and a list of space separated integers (0 or 1). The goal is to
count the minimum number of jumps required to read the end avoiding all 1's.
Jumps can be of 1 or 2 numbers.
"""


def jumping_on_c(c):
    idx = 0
    jumps = 0

    # len has cost O(1) https://wiki.python.org/moin/TimeComplexity
    # Can invert if statements with idx + 2 == len(c) or c[idx + 2]
    while idx < len(c)-1:
        if c[idx+1] or (idx+2 < len(c) and not c[idx+2]):
            idx += 2
        else:
            idx += 1
        jumps += 1

    return jumps
        


if __name__ == '__main__':
    n = int(input())
    c = list(map(int, input().rstrip().split()))

    print(jumping_on_c(c))
