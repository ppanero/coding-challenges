#!/bin/python3

"""
Given a list of comma separated numbers, representing people in a queue,
calculate the minimum number of swaps (bribes) to reach the current state.
If a person bribed more than twice, it should output 'Too chaotic'.
"""

# O(n^2) solution, O(n)?
def minimum_bribes(q):
    bribes = 0
    for idx, person in enumerate(q):
        diff = person - (idx + 1)
        if diff > 2:
            print("Too chaotic")
            return  # Not a fan of breaking like this tho
        for j in range(max(person-2,0), idx):
            if q[j] > person:
                bribes += 1
    print(bribes)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))

    minimum_bribes(q)
