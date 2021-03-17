#!/bin/python3

"""
Sherlock considers a string to be valid if all characters of the string
appear the same number of times. It is also valid if he can remove just 1
character, and the remaining characters will occur the same number of times.
Given a string, determine if it is valid. If so, return YES, otherwise return
NO.
"""

from collections import Counter


def is_valid(s):
    # breakpoint()
    appearances = sorted(Counter(s).values())
    exception = False

    if len(appearances) > 1 and appearances[0] == 1:
        if appearances[1] != 1:
            exception = True
        appearances = appearances[1:]  # Remove the case when one letter appears once

    previous = appearances[0]
    for num in appearances[1:]:
        if previous + 1 < num:
            print("NO")
            return  # Not a fan of breaking like this tho
        elif previous + 1 == num:
            if not exception:
                exception = True
            else:
                print("NO")
                return
    print("YES")

if __name__ == '__main__':
    s = input()

    is_valid(s)
