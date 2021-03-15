#!/bin/python3

"""
Given a list of comma separated numbers sort them in ascending order,
by swaping any two elements. Print the minimum number of swaps needed.
"""

def minimum_swaps(arr):
    swaps = 0
    idx = 0
    while idx < len(arr)-1:
        true_idx = arr[idx]-1
        if arr[idx] != arr[true_idx]:
            arr[idx], arr[true_idx] = arr[true_idx], arr[idx]
            swaps += 1
        else:
            idx += 1
    
    return swaps

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    print(minimum_swaps(arr))
