#!/bin/python3

"""
Given an array of integers and a target value, determine the number of pairs
of array elements that have a difference equal to the target value.
"""

# Not good enough for the time limitations
# from itertools import combinations
#
# def pairs(k, arr):
#     combs = combinations(arr, 2)
#
#     total = 0
#     for comb in combs:
#         if abs(comb[0] - comb[1]) == k:
#             total += 1
#       
#     return total

# A bit better
# def pairs(k, arr):
#     arr.sort()
#
#     total = 0
#     for idx, val in enumerate(arr):
#         j = idx + 1
#         diff = 0
#         while j < len(arr) and diff < k:
#             diff = arr[j] - val
#             if diff == k:
#                 total += 1
#             j += 1
# 
#     return total


# Using hashmaps (dicts)
# from collections import Counter
#
# def pairs(k, arr):
#     keys = Counter(arr)
#     total = 0
#     for val in arr:
#         if keys[val + k] > 0:
#             total += 1
#
#     return total


# Bit wise operations
def pairs(k, arr):
    nums = set(arr)
    # Make a set of all required nums that satisfy the diff: arr[i] + k
    needed = set(num + k for num in arr)
    # Return the length of the intersection set
    # That is the length of the needed that are in the origial (nums)
    return len(nums&needed)


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))

    print(pairs(k, arr))