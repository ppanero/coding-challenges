#!/bin/python3

"""
Given two strings, check if they share a substring. A single character
is considered to be a substring.
"""


def two_strings(s1, s2):
    # Could be done as set intersection.
    # Bitwise AND is enough, it actually returns a dict of the substring.
    if set(s1) & set(s2):
        return "YES"
    else: 
        return "NO"

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s1 = input()
        s2 = input()
        print(two_strings(s1, s2))
