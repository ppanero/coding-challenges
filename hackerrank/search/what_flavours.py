#!/bin/python3

"""
Given an unordered array of integers representing the cost of the flavour
identified by index+1, get the identifier of those two flavours that would
consume the whole of the available money.
"""

from collections import Counter

def what_flavors(cost, money):
    
    # Keep track of all the indices
    indices = {}
    for idx, elem in enumerate(cost):
        if indices.get(elem):
            # Needs to be array cuz there might be repeated
            indices[elem].append(idx+1)
        else:
            indices[elem] = [idx+1]

    times = Counter(cost)

    for idx, val1 in enumerate(cost):
        val2 = money - val1  # Asume cannot be negative
        if val1 != val2:
            if times[val2] > 0:
                idx2 = indices[val2].pop()
                print(f"{idx+1} {idx2}") if idx+1 <= idx2 else print(f"{idx2} {idx+1}")
                return
        else:
            if times[val1] > 1:
                idx2 = indices[val2].pop()
                print(f"{idx+1} {idx2}") if idx+1 <= idx2 else print(f"{idx2} {idx+1}")
                return


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())
        n = int(input())
        cost = list(map(int, input().rstrip().split()))

        what_flavors(cost, money)
