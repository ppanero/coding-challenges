#!/bin/python3

"""
A small frog wants to get to the other side of the road. The frog is currently
located at position X and wants to get to a position greater than or equal to
Y. The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.
"""

def num_jumps(X, Y, D):
    diff = Y - X
    jumps = diff // D
    
    return jumps if not diff % D else jumps + 1

# Example execution
# (1, 7, 2) --> 3 (reaches 7)
# (0, 7, 2) --> 4 (reaches 8)