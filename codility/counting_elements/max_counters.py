#!/bin/python3

"""
You are given N counters, initially set to 0, and you have two possible
operations on them:
- increase(X) − counter X is increased by 1,
- max counter − all counters are set to the maximum value of any counter.

A non-empty array A of M integers is given. This array represents consecutive
operations:
- if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
- if A[K] = N + 1 then operation K is max counter.
"""

def max_counters(N, A):
    counters = [0] * N
    max_ctr = 0

    for idx, op in enumerate(A):
        if op != N+1:
            # Assumes op <= N always
            counters[op-1] += 1
            if counters[op-1] > max_ctr:
                max_ctr = counters[op-1]
        else:
            counters = [max_ctr] * N

    return counters
