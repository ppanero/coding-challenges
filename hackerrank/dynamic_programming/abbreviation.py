#!/bin/python3

"""
You can perform the following operations on the string, a:
- Capitalize zero or more of a's lowercase letters.
- Delete all of the remaining lowercase letters in a.
Given two strings, a and b, determine if it's possible to make a equal to b as
described. If so, print YES on a new line. Otherwise, print NO.
"""

from collections import defaultdict, Counter

def abbreviation(a, b):
    if len(a) < len(b):
        print("NO")
    
    # Create a matrix with a padding of one
    achievable = []
    for idx_i in range(len(a)+1):
        achievable.append([])
        for idx_j in range(len(b)+1):
            achievable[idx_i].append(False)

    # Traverse the grid
    # Index handling could be optimized with a few breaks?
    achievable[0][0] = True
    for idx_i, val_a in enumerate(a):
        for idx_j in range(len(b)+1):
            if achievable[idx_i][idx_j]:
                if idx_j < len(b) and val_a.upper() == b[idx_j]:
                    achievable[idx_i + 1][idx_j + 1] = True
                if not val_a.isupper():
                    achievable[idx_i + 1][idx_j] = True

    return "YES" if achievable[len(a)][len(b)] else "NO"

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        a = input()
        b = input()

        print(abbreviation(a, b))
