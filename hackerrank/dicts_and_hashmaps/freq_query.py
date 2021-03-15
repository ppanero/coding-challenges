#!/bin/python3

"""
The queries are of the form (action, value). The actions can be:
1- Insert the value in the data structure
2- Remove an appearance of the value from the data structure
3- If an element in the data structure has the value frequence print 1 else 0
"""

from collections import defaultdict


def freq_query(queries):
    elements = defaultdict(int)
    frequencies = defaultdict(int)
    for query in queries:
        if query[0] == 1:
            freq = elements[query[1]] + 1
            elements[query[1]] = freq
            frequencies[freq] += 1
            if freq - 1 > 0:
                frequencies[freq-1] = max(0, frequencies[freq-1] - 1)
        elif query[0] == 2:
            freq = elements.get(query[1])
            if freq:
                elements[query[1]] = freq -1
                frequencies[freq] = max(0, frequencies[freq] - 1)
                if freq - 1 > 0:
                    frequencies[freq-1] += 1
        elif query[0] == 3:
            result = 1 if frequencies.get(query[1]) else 0
            print(result)

if __name__ == '__main__':
    q = int(input().strip())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    freq_query(queries)
