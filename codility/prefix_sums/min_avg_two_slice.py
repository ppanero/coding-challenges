#!/bin/python3

"""
Given an array of integers, give the lowest index that starts
the slice of minimal average, being it the sum of its numbers
divided by the amount of numbers in the slice.
"""

# Basically it shows that the lowest avg slice contains a slice
# of minimal avg of lenght 2 or 3
def min_avg_slice(A):
    # Could be done with two for loops O(N^2)
    min_avg_value = (A[0] + A[1])/2.0   # The mininal average
    min_avg_pos = 0     # The begin position of the first
                        # slice with mininal average
    for index in range(0, len(A)-2):
        # Try the next 2-element slice
        if (A[index] + A[index+1]) / 2.0 < min_avg_value:
            min_avg_value = (A[index] + A[index+1]) / 2.0
            min_avg_pos = index
        # Try the next 3-element slice
        if (A[index] + A[index+1] + A[index+2]) / 3.0 < min_avg_value:
            min_avg_value = (A[index] + A[index+1] + A[index+2]) / 3.0
            min_avg_pos = index
    # Try the last 2-element slice
    if (A[-1]+A[-2])/2.0 < min_avg_value:
        min_avg_value = (A[-1]+A[-2])/2.0
        min_avg_pos = len(A)-2
    return min_avg_pos