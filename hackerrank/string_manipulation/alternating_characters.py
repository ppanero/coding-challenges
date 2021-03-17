#!/bin/python3

"""
Given a string with A's and B's count the minimum number of deletions required
to convert it into a string with no equal adjacent characters.
"""

def alternating_characters(s):
    deletions = 0
    previous = s[0]
    for char in s[1:]:
        if char == previous:
            deletions += 1
        else:
            previous = char
    
    return deletions


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()
        print(alternating_characters(s))
