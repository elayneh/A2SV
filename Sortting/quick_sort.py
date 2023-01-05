# usr/bin/python3
from random import randint

"""An example of divivde and conquer algorithmic technique
also called partition exchange sort
Divide: The given arrayA[low...high] is partitioned into 2 non empty arraysA[low...q] and A[q+1...high]
Conquer: The 2 sub arrays A[low...q] and A[q+1...high] are sorted by recursive calls to Quick sort.
"""

def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)

    return arr

def partition(arr, low, high):
    pivot = low
    swap(arr, pivot, high)
    for i in range(low, high):
        if arr[i] <= arr[high]:
            swap(arr, i, low)
            low += 1
    swap(arr, low, high)
    return low

def swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp


if __name__== "__main__":
    arr = [randint(10, 100) for i in range(10)]
    original_array = arr
    sorted_array = quickSort(arr, 0, len(arr) - 1)
    print("Original array: {}".format(original_array))
    print("Sorted array: {}".format(sorted_array))
