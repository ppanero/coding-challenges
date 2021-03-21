#!/bin/python3

"""
Given an array A of N integers, returns the smallest positive integer (greater
than 0) that does not occur in A.
"""

def min_pos_missing(A):
    nums = set()
    for num in A:
        if num > 0:
            nums.add(num)
    
    count = 1
    for i in range(len(nums)):
        if not count in nums:
            return count
        count +=1

    return count

# Example execution
# [1,2,3,5] --> 4
# [-3, -2] --> 1
# [-3, -2, 0, 4, 3] --> 1
# [1, 2, 3, 4, 5, 6] --> 7