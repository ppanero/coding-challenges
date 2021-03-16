#!/bin/python3

"""
Implement merge sort and count the number of inversions.
"""


def merge_halves(left, right):
    invs = 0
    sorted_arr = []
    
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            sorted_arr.append(right[j])
            invs += (len(left) - i)
            j += 1
        else:
            sorted_arr.append(left[i])
            i += 1
    
    if len(left) - i > 0:
        sorted_arr += left[i:]
    elif len(right) - j > 0:
        sorted_arr += right[j:]
    
    return invs, sorted_arr



def sort_and_count_inv(arr):
    if len(arr) < 2:
        return 0, arr

    if len(arr) == 2:
        if arr[1] < arr[0]:
            return 1, [arr[1], arr[0]]
        else:
            return 0, arr
        
    half = len(arr) // 2
    breakpoint()
    left_inv, left = sort_and_count_inv(arr[:half])
    right_inv, right = sort_and_count_inv(arr[half:])
    merge_inv, arr = merge_halves(left, right)
    
    invs = left_inv + right_inv + merge_inv

    return invs, arr



def count_inversions(arr):
    invs, sorted_arr = sort_and_count_inv(arr)
    return invs


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())
        arr = list(map(int, input().rstrip().split()))

        print(count_inversions(arr))
