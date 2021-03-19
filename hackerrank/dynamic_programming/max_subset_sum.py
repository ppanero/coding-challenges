#!/bin/python3

"""
Given an array of integers, find the subset of non-adjacent elements with the
maximum sum. Calculate the sum of that subset. It is possible that the maximum
sum is 0, the case when all elements are negative.

Example execution:

3 5 -7 8 10

3  [3, 5, -7, 8, 10]
5  [3, 5, -7, 8, 10]
-7 [3, 5, -7, 8, 10]
8  [3, 5, 5, 8, 10]
10 [3, 5, 5, 13, 10]
10 [3, 5, 5, 13, 15]

Resutlt --> 15
"""

def max_subset_sum(arr):
    arr[0] = max(0, arr[0])  # Empty subset is an option
    if len(arr) == 1: # Empty array is not an option
        return arr[0]

    arr[1] = max(arr[:2])
    for idx, num in enumerate(arr[2:], start=2):
        arr[idx] = max(arr[idx-1], arr[idx-2], num + arr[idx-2], num)

    return arr[-1]


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    
    print(max_subset_sum(arr))
