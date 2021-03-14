#!/bin/python3

"""
Input the lenght and a list of space separated integers, representing socks
colors. Count how many are paired.
"""

from collections import Counter

   
def sock_merchant(n, ar):
    c = Counter(ar)
    pairs = 0

    for num in c:
        pairs += c[num] // 2

    return pairs

      
if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))

    print(sock_merchant(n, ar))
