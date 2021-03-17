#!/bin/python3

"""
A string can be subject to three operations: revers, shuffle or merge.
Given a string s belonging to all possibilityes of 
merge(reverse(A), shuffle(A)). Find the lexicographically smalles A.
"""

from collections import defaultdict, Counter

def reverse_shuffle_merge(s):
    chars = Counter(s)
    remaining = dict(chars)
    used = defaultdict(int)
    needed = {}

    for char, amount in chars.items():
        needed[char] = amount // 2
    
    def can_use(char):
        return needed[char] - used[char] > 0 

    def can_remove(char):
        return used[char] + remaining[char] - needed[char] >= 1

    word = [s[-1]]
    used[s[-1]] += 1
    remaining[s[-1]] -= 1
    for char in reversed(s[:-1]):
        if can_use(char):
            while word and word[-1] > char and can_remove(word[-1]):
                removed_char = word.pop()
                used[removed_char] -= 1
            
            used[char] += 1
            word.append(char)
        
        remaining[char] -= 1
        
    return "".join(word)


if __name__ == '__main__':
    s = input()

    print(reverse_shuffle_merge(s))
