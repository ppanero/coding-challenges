#!/bin/python3

"""
Given two sentences, the first representing the available words on a magazine
and the second the words needed to write a ransom note. Check if said note can
be writte. Take into account that words are case sensitive.
"""

from collections import Counter

def check_magazine(magazine, note):
    can_wrinte = "Yes" if Counter(note) - Counter(magazine) == {} else "No"
    print(can_wrinte)
    

if __name__ == '__main__':
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    magazine = input().rstrip().split()
    note = input().rstrip().split()
    check_magazine(magazine, note)
