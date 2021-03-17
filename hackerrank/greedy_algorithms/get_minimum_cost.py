#!/bin/python3

"""
Given a list of prices of the flowers and a number of buyers, calculate
the minimum cost possible taking into account the cost of each flower is:

(#flowers already bought + 1) * cost of the flower
"""


def get_minimum_cost(k, c):
    c.sort(reverse=True)
    cost = sum(c[:k])

    bought_counter = 0
    for idx, flower_cost in enumerate(c[k:], start=k):
        curr_counter = idx // k
        if bought_counter < curr_counter:
            bought_counter = curr_counter
        
        cost += (bought_counter + 1) * flower_cost 

    return cost



if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))

    print(get_minimum_cost(k, c))
