#!/bin/python3

"""
Given an array of integers representing the places where a leaf falls,
calculate the time when there are leaves in positions 1 to X (included).
Return -1 if not possible.
"""

def frog_river_one(A, X):
    leaves = set()
    for pos in range(1, X+1):
        leaves.add(pos)
    
    for idx, time in enumerate(A):
        try:
            leaves.remove(time)
        except KeyError:
            pass  # Multiple leaves in a position
        if len(leaves) == 0:
            return idx
    
    return -1

# Example execution
# [(1, 3, 1, 4, 2, 3, 5, 4), X = 5] --> 6
