#!/bin/python3

"""
We define the following:
- A subarray of array a of length n is a contiguous segment from a[i] through
  a[j] where 0 <= i <=j < n.
- The sum of an array is the sum of its elements.

Given an  element array of integers and an integer, m, determine the maximum
value of the sum of any of its subarrays modulo m. 
"""

# Brute force case, not efficient
def maximum_sum(a, m):
    total = 0
    i = 0
    while total < m and i < len(a):
        for idx in range(0, i):
            curr = sum(a[idx:i+1]) % m
            if curr > total:
                total = curr
        i += 1
    return total

# Better answer using modular arithmetics here
# https://www.quora.com/What-is-the-logic-used-in-the-HackerRank-Maximise-Sum-problem

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        nm = input().split()
        n = int(nm[0])
        m = int(nm[1])
        a = list(map(int, input().rstrip().split()))

        print(maximum_sum(a, m))
