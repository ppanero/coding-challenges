#!/bin/python3

"""
You are planning production for an order. You have a number of machines that
each have a fixed number of days to produce an item. Given that all the
machines operate simultaneously, determine the minimum number of days to
produce the required order.
"""

#from bisect import bisect
#
# Not efficient enough
# def min_time(machines, goal):
#     machines.sort()
#     total = 0
#     days = 0
#     while total < goal:
#         # Start in 0 makes no sense
#         # and if total is reach dont need to increase days after
#         days += 1
#         # Right most index (in case of equals) of the machines that could
#         # have produced an item
#         lower = bisect(machines, days)
#         for machine in machines[:lower]:
#             if not days % machine:
#                 print(machine, days)
#                 total += 1
#     return days


# This approach performs binary search over the amount of days.
# Uses a hash map to calculate the amount of items produced within it.
from math import ceil
from collections import Counter

def min_time(machines, goal):
    inventory = Counter(machines)
    fastest = min(inventory)
    min_days = 1
    # Amount of days if items were to be produced with the fastest machine
    max_days = ceil( (goal / inventory[fastest]) * fastest)
    
    while max_days - min_days>1:
        mid = (min_days+max_days) // 2

        total = sum( (mid // days) * mach for days, mach in inventory.items())
        
        if total < goal:
            min_days = mid
        else:
            # Since this will end up in max = min
            # It is the same as returning or flagging found
            max_days = mid

    return max_days

if __name__ == '__main__':
    n_goal = input().split()
    n = int(n_goal[0])
    goal = int(n_goal[1])
    machines = list(map(int, input().rstrip().split()))
    
    print(min_time(machines, goal))
