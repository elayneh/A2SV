# usr/bin/python3

"""Works well for small files(with large value and small keys)
Requires no additional storage space
Doesn't scale well O(n2)
"""
from random import randint


def selectionSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr

print(selectionSort([randint(10, 100) for i in range(10)]))
