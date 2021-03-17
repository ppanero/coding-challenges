#!/bin/python3

"""
Given a list of integers and a number k, create an array of length k whose
unfairness is minimized. The unfairness of the array is max(arr) - min(arr).
"""

def max_min(k, arr):
    arr.sort(reverse=True)
    
    unfairness = arr[0] - arr[k-1]
    for idx in range(1, len(arr)-k+1):
        curr_unfairness = arr[idx] - arr[idx+k-1]
        if curr_unfairness < unfairness:
            unfairness = curr_unfairness
    
    return unfairness

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    print(max_min(k, arr))
