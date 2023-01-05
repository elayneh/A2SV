# usr/bin/python3
from random import randint

"""is used when the data is nearly sorted or when the input size is small
worst case complexity: O(n2)
best case complexity: n
"""
def insertion_sort(arr):
    for i in range(1, len(arr)):
        target = arr[i]
        hole = i
        print(arr)
        while hole > 0 and target < arr[hole - 1]:
            arr[hole] = arr[hole - 1]
            hole -= 1

        arr[hole] = target
        print(arr)

    return arr

if __name__ == "__main__":
    original_array = arr = [randint(10, 100) for i in range(10)]
    print("Original array: {}".format(original_array))
    sorted_array = insertion_sort(arr)
    print("Sorted array: {}".format(sorted_array))
