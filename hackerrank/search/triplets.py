#!/bin/python3

"""
Given 3 arrays a, b and c of different sizes, find the number of distinct
triplets (p, q, r) where p is an element of a, q of b and r of c and
satisfying that p <= q and q >= r.
"""

# Not efficient enough
# def triplets(a, b, c):
#     a = sorted(list(set(a)))
#     b = sorted(list(set(b)), reverse=True)
#     c = sorted(list(set(c)))
#
#     count = 0
#     for p in a:
#         i = 0
#         while i < len(b) and b[i] >= p:
#             j = 0
#             while j < len(c) and b[i] >= c[j]:
#                 count += 1
#                 j += 1
#             i += 1
#
#     return count


# def triplets(a, b, c):
#     a = sorted(list(set(a)))
#     b = sorted(list(set(b)))
#     c = sorted(list(set(c)))
# 
#     count = 0
#     for q in b:
#         i = 0
#         j = 0
#         while i < len(a) and a[i] <= q:
#             i += 1
#         while j < len(c) and c[j] <= q:
#             j += 1    
#         count += i * j
#     return count


# Same as above but position calculation is done by bisect (binary search)
from bisect import bisect

def triplets(a, b, c):
    a = sorted(list(set(a)))
    b = sorted(list(set(b)))
    c = sorted(list(set(c)))

    count = 0
    for q in b:
        count += bisect(a, q) * bisect(c, q)

    return count

if __name__ == '__main__':
    lenaLenbLenc = input().split()
    lena = int(lenaLenbLenc[0])
    lenb = int(lenaLenbLenc[1])
    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))
    arrb = list(map(int, input().rstrip().split()))
    arrc = list(map(int, input().rstrip().split()))

    print(triplets(arra, arrb, arrc))