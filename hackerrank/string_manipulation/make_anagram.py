#!/bin/python3

"""
Two strings are anagrams when they contain the same characters with the same
frequency. Calculate the minimum number of characters to remove from them
so they are anagrams.
"""

from collections import Counter

def make_anagram(a, b):
    chars_a = Counter(a)
    chars_b = Counter(b)
    to_remove = 0

    for char, amount_a in chars_a.items():
        amount_b = chars_b.get(char)
        if not amount_b :
            to_remove += amount_a
        else:
            to_remove += abs(amount_a - amount_b)
            chars_b.pop(char)
    
    for char, amount_b in chars_b.items():
        to_remove += amount_b
    
    return to_remove


if __name__ == '__main__':
    a = input()
    b = input()

    print(make_anagram(a, b))
