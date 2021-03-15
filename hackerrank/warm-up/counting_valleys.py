#!/bin/python3

"""
Input a length and a string of up (U) and downs (D). A valley starts and ends
at sea level (0). Count the number of valleys the hiker goes through.
"""


def counting_valleys(steps, path):
    level = 0
    valleys = 0
    for step in range(steps):
        level += 1 if path[step] == "U" else -1
        if path[step] == "U" and level == 0:
            valleys += 1
    
    return valleys


if __name__ == '__main__':
    steps = int(input().strip())
    path = input()

    print(counting_valleys(steps, path))
