#!/bin/python3

"""
Implement bubble sort and count the amount of swaps needed to sort an array.
"""

def count_swaps(a):
    swaps = 0 
    for i in range (0, len(a)):
        for j in range(0, len(a)-1):
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1
    print(f"Array is sorted in {swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[len(a)-1]}")


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().rstrip().split()))

    count_swaps(a)


