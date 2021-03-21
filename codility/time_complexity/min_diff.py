#!/bin/python3

"""
Given an array of integers and a difference the absolute difference of the
left and right side. Calculate the minimum difference.
"""

def difference(A):
    left = A[0]
    right = sum(A[1:])
    min_diff = abs(left - right)
    
    for num in A[1:-1]:
        left += num
        right -= num
        curr_diff = abs(left - right)
        if curr_diff < min_diff:
            min_diff = curr_diff

    return min_diff

# Example execution:
# (3, 1, 2, 3, 4) --> 1 (|6 - 7|, from (3+1+2)-(3+4))

print(difference([3,4]))