#!/bin/python3

"""
There are 16 hourglasses in a 6x6 array. An hourglass sum is the sum of an
hourglass' values (of an inner 3x3, the 3 top plus 3 bottom plus the middle
one of the middle row). Calculate the hourglass sum for every hourglass,
then print the maximum hourglass sum. The array will always be 6x6.
"""


def hourglass_sum(arr):
    # From description lowest is -9 and an hourglass has 7 values
    max_sum = -9 * 7

    for i in range(4):
        for j in range(4):
            top = sum(arr[i][j:j+3])
            middle = arr[i+1][j+1]
            bottom = sum(arr[i+2][j:j+3])

            total = top + middle + bottom
            if total > max_sum:
                max_sum = total
    
    return max_sum


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(hourglass_sum(arr))
