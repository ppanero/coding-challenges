#!/bin/python3

"""
Given a list of contests, with a luck amount and an importance (0, 1).
If the contest is won, the luck is substracted, otherwise summed up.
What is the maximum luck that one can accumulate by only loosing a
max of k important contests.
"""

from bisect import insort


def luck_balance(k, contests):
    important_luck_sorted = []
    luck = 0
    for data in contests:
        if data[1] == 0:  # Not important -> lose it
            luck += data[0]
        else:
            insort(important_luck_sorted, data[0])

    if len(important_luck_sorted) <= k:
        luck += sum(important_luck_sorted)
    else:
        idx = len(important_luck_sorted) - k
        luck += sum(important_luck_sorted[idx:])
        luck -= sum(important_luck_sorted[:idx])

    return luck

if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    print(luck_balance(k, contests))
