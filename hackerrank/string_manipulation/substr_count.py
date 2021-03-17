#!/bin/python3

"""
A string is said to be a special string if either of two conditions is met:
- All of the characters are the same, e.g. aaa.
- All characters except the middle one are the same, e.g. aadaa.
Given a string and length (n), count the amount of substrings of length n.
"""

# Not efficient enough for the tests 7/17 timed out
# def substr_count(n, s):
#     specials = len(s)  # Each single char
#     for i, init_val in enumerate(s):
#         diff_char_idx = None
#         for j, end_val in enumerate(s[i+1:], start=i+1):
#             if init_val == end_val:
#                 if diff_char_idx is None:
#                     specials +=1
#                 elif j - diff_char_idx == diff_char_idx - i:
#                     specials += 1
#             else:
#                 if diff_char_idx is None:  # avoid issues when = 0
#                     diff_char_idx = j
#     return specials

def substr_count(n, s):
    specials = 0
    same_chars_count = [1] * len(s)

    # Sum all occurences of consecutive characters
    prev_char = s[0]
    k = 1
    for idx, char in enumerate(s[1:], start=1):
        if char == prev_char:
            k += 1
            same_chars_count[idx] = k
        elif char != prev_char:
            prev_char = char
            specials += (k * (k + 1)) // 2
            k = 1
    
    specials += (k * (k + 1)) // 2

    # Sum occurences with a different middle char
    for idx in range(len(s)-2, 0, -1):
        if s[idx] == s[idx+1]:
            same_chars_count[idx] = same_chars_count[idx+1]
        elif s[idx-1] == s[idx+1] != s[idx]:
            specials += min(same_chars_count[idx-1], same_chars_count[idx+1])

    return specials


if __name__ == '__main__':
    n = int(input())
    s = input()

    print(substr_count(n, s))
