#!/usr/bin/python3
from random import randint

"""is used when the data is nearly sorted or when the input size is small
worst case complexity: O(n2)
best case complexity: n
"""
def insertion_sort(arr):
   for i in range(len(arr)):
        target = i
        while arr[target] < arr[target - 1] and target > 0:
            arr[target], arr[target - 1] = arr[target - 1], arr[target]
            target -= 1

        if i > 0:
            print(*arr)

if __name__ == "__main__":
    original_array = arr = [randint(10, 100) for i in range(10)]
    insertion_sort([3, 4, 7, 5, 6, 2, 1])
