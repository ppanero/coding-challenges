#!/bin/python3

"""
Given the number of trailing days, d, and a client's total daily expenditures
for a period of n days, determine the number of times the client will receive
a notification over all  days.
A client will be notified if the amount spent on a day is equal or higher than
twice the median of the previous d days.
"""

# Not efficient due to multiple sorting
# def median(arr):
#     if len(arr) % 2:
#         return arr[len(arr)//2]  # zero index, then e.g. 7 // 2 = 3
#     half = len(arr) // 2
#     return (arr[half] + arr[half-1]) / 2
# def activity_notifications(expenditure, d):
#     notif = 0
#     idx = d
#     previous = sorted(expenditure[:d])
#     while idx < len(expenditure):
#         if expenditure[idx] >= (2*median(previous)):
#             notif += 1
#         idx += 1
#         previous = sorted(expenditure[idx-d:idx])
#     return notif

# Efficient, using bisect
# from bisect import bisect, insort
#
# def activity_notifications(expenditure, d):
#     notif = 0
#     previous = sorted(expenditure[:d])
#     for idx, val in enumerate(expenditure[d:]):
#         if d % 2:
#             limit = 2*previous[d//2]
#         else:
#             limit = previous[d//2] + previous[d//2-1]
#         if val >= limit:
#             notif += 1
#
#         # Update previous
#         del_idx = bisect(previous, expenditure[idx])
#         previous.pop(del_idx-1)
#         insort(previous, val)
#
#     return notif

def twice_median(arr, d):
    curr_total = 0
    val1, val2 = None, None
    med_idx1, med_idx2 = d//2, d//2+1

    for idx, val in enumerate(arr):
        curr_total += val
        if not val1 and curr_total >= med_idx1:
            val1 = idx
        if curr_total >= med_idx2:
            val2 = idx
            break

    return (val2 * 2) if d % 2 else (val1 + val2)


def activity_notifications(expenditure, d):
    notif = 0
    count = [0] * (max(expenditure)+1)  # Count sort appearances
    # Initialize count sort
    for elem in expenditure[:d]:
        count[elem] += 1

    for idx, val in enumerate(expenditure[d:]):
        if val >= twice_median(count, d):
            notif += 1
        # Update count sort
        count[expenditure[idx]] -= 1  # idx starts in zero (real idx - d)
        count[val] += 1
    return notif


if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    expenditure = list(map(int, input().rstrip().split()))

    print(activity_notifications(expenditure, d))
