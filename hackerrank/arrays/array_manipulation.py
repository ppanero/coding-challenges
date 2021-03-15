#!/bin/python3

"""
Given a list of operations defined as (start index, end index, value) sum up
the value to all index positions between the start and end index. Note that 
those indexes start in 1. Return the maximum value of the resulting array.
"""

import itertools

# Trivial but requires more resources than allocated.
# def array_manipulation(n, queries):
#     array = [0] * n  # Create 0-filled array or length n
#     max_val = 0  # Cuz max() is O(n)
#     for query in queries:
#         for i in range(query[0]-1, query[1]):
#             array[i] += query[2]
#             if array[i] > max_val:
#                 max_val = array[i]
#     return max_val

def array_manipulation(n, queries):
    array = [0] * n  # Create 0-filled array or length n
    for query in queries:
        array[query[0] - 1] += query[2]
        if query[1] < n:
            array[query[1]] -= query[2]  # To compensate on accumulate
    # Could do a manual loop and do O(n) instead of O(n*n)
    return max(itertools.accumulate(array))


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    print(array_manipulation(n, queries))
