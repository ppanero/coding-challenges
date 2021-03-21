#!/bin/python3

"""
Given a list of nucleoids (A, C, G, T) with values 1, 2, 3, 4. Given a list of
ranges (P[i], Q[i]) return the lowest value available in it (e.g. 1 if there 
is an A in said range).
"""

def genomic_range_query(S, P, Q):
    A = [-1] * len(S)
    C = [-1] * len(S)
    G = [-1] * len(S)
    T = [-1] * len(S)

    for idx, nucl in enumerate(S):
        A[idx] = A[idx-1]
        C[idx] = C[idx-1]
        G[idx] = G[idx-1]
        T[idx] = T[idx-1]
        if nucl == "A":
            A[idx] = idx
        elif nucl == "C":
            C[idx] = idx
        elif nucl == "G":
            G[idx] = idx
        elif nucl == "T":
            T[idx] = idx
    
    results = [0] * len(P)

    for idx, p in enumerate(P):
        if A[Q[idx]] >= p:
            results[idx] = 1
        elif C[Q[idx]] >= p:
            results[idx] = 2
        elif G[Q[idx]] >= p:
            results[idx] = 3
        elif T[Q[idx]] >= p:
            results[idx] = 4

    return results
