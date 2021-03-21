#!/bin/python3

"""
Given an integer array A and a number K, perform K left rotations.
"""

def right_rotate(A, K):
    # Be careful the mod operation fails when array is empty
    # if not len(A):
    #   return A
    limit = K % len(A)
    return A[-limit:] + A[:-limit]


# Example test cases:
# ([1, 2 ],2) --> [1, 2]
# ([1, 2, 3, 4, 5], 4) -> [2, 3, 4, 5, 1]
# ([1, 2], 3) --> [2, 1], This use case shows the importance of the modulo op