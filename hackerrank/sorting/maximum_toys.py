#!/bin/python3

"""
Given a list of prices of toys and an amount of money, maximize the number
of toys that can be bought.
"""


def insert_in_place(arr, val):
    idx = 0
    higher = False
    # breakpoint()
    while idx  < len(arr) and not higher:
        if val < arr[idx]:
            higher = True
        else:
            idx +=1

    return arr[:idx]+[val]+arr[idx:]


def maximum_toys(prices, k):
    toys = []
    accumulated = 0
    
    for price in prices:
        if price + accumulated < k:
            toys = insert_in_place(toys, price)
            accumulated += price
        elif len(toys) and price < toys[len(toys)-1] and price + accumulated - toys[len(toys)-1] < k:
            # breakpoint()
            accumulated = price + accumulated - toys[len(toys)-1]
            toys = insert_in_place(toys[:-1], price)
    
    return len(toys)


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    prices = list(map(int, input().rstrip().split()))

    # Sorting the array at the beggining would avoid the ordered insert.
    # However, if the array is long, and the amount of toys are small
    # ordered insert might be more efficient, and fun to code.
    print(maximum_toys(prices, k))
