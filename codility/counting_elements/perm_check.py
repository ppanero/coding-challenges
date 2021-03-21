#!/bin/python3

"""
Given an array of integers representing the places where a leaf falls,
calculate the time when there are leaves in positions 1 to X (included).
Return -1 if not possible.
"""

# Checking if the sum of the elements is equal to what it should
# (i.e. n*(n+1)//2) would not work because numbers can be compensated.
# It needs to check for exact existance.
def perm_check(A, X):
    nums = set()
    for i in range(1, len(A)+1):
        nums.add(i)
    
    for num in A:
        try:
            nums.remove(num)
        except KeyError:
            pass   # Repeated or out of range numbers
    
    return 1 if not len(nums) else 0

# Example execution
# (4, 3, 1, 2) --> 1
# (4, 1, 3) --> 0 (Should not contain 4, but contain 2)
 