#!/bin/python3

"""
A string is said to be a child of a another string if it can be formed by
deleting 0 or more characters from the other string. Letters cannot be
rearranged. Given two strings of equal length, what's the longest string that
can be constructed such that it is a child of both?
"""

# This is a case of LCS (Longest Common Subsequence) problem
# https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
# Tutorial https://www.youtube.com/watch?v=FWyANT-7iq8
def common_child(s1, s2):
    vert, horiz = len(s1), len(s2)
    matrix = [ [0]*(horiz+1) for times in range(vert+1) ]

    for i, val_v in enumerate(s1):
        for j, val_h in enumerate(s2):
            if val_v == val_h:
                # Set positions + 1 but compare positions
                # because there is one ghost row/column at
                # the beginning
                matrix[i+1][j+1] = matrix[i][j] + 1
            else:
                matrix[i+1][j+1] = max(matrix[i][j+1], matrix[i+1][j])
    
    return matrix[-1][-1]


if __name__ == '__main__':
    s1 = input()
    s2 = input()

    print(common_child(s1, s2))
