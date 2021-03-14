#!/bin/python3

"""
Two strings are anagrams of each other if the letters of one string can be
rearranged to form the other string. Given a string, find the number of
pairs of substrings of the string that are anagrams of each other.

s = "mom"
The list of all anagrammatic pairs is [m,m], [mo, om] at positions [[0],[2]], [[0,1],[1,2]] respectively.
"""

from collections import defaultdict


def sherlock_and_anagrams(s):
    parts = defaultdict(list)
    for idx, char in enumerate(s):
        current = char
        parts[char].append(len(parts[char])+1)
        for j in range(idx+1, len(s)):
            current = ''.join(sorted(current + s[j]))
            parts[current].append(len(parts[current])+1)

    total_anagrams = 0
    for val in parts.values():
        if len(val) > 1:
            total_anagrams += sum(val[:-1])
    
    return total_anagrams


if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()
        print(sherlock_and_anagrams(s))
