#!/usr/bin/python3

# This is Phase 1 to implement count sorting algorithm
def countingSort(arr):
    aarr = [0]*(max(arr) + 1)
    for item in arr:
        aarr[item] += 1

    return aarr
