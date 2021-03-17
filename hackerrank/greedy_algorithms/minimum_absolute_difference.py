#!/bin/python3

"""
Given an array of integers calculate the minimum absolute difference between
any pair of numbers.
"""

def minimum_absolute_difference(arr):
    arr.sort()

    min_diff = abs(arr[1] - arr[0])
    prev = arr[1]
    for num in arr[2:]:
        local_diff = abs(prev - num)
        if local_diff < min_diff:
            min_diff = local_diff
        prev = num
    
    # Could use min:
    # min_diff = min(abs(arr[i+1]-arr[i]) for i in range(len(arr)-1))

    return min_diff


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    print(minimum_absolute_difference(arr))
