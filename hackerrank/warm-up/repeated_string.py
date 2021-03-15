#!/bin/python3

"""
There is a string of lowercase English letters that is repeated infinitely
many times. Given an integer, n, find and print the number of letter a's in
the first n letters of the infinite string.
"""


def repeated_string(s, n):
    num_a = n // len(s) * s.count('a')  # Could use re.findall, whats better?
    extra = n % len(s)
    if extra:
        num_a += s[:extra].count('a')
    
    return num_a

if __name__ == '__main__':
    s = input()
    n = int(input())

    print(repeated_string(s, n))
