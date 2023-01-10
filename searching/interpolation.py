#usr/bin/python3

from random import randint

"""
"""

def interpolationSearch(arr, key):
    low = 0
    high = len(arr) - 1
    while arr[low] <= key and arr[high] >= key:
        middle = low + ((key - arr[low]) - (high - low)) // (arr[high] - arr[low])
        if arr[middle] == key:
            print("{} is found at the position {} in the array: {}".format(key, middle, arr))
            return
        elif arr[middle] < key:
            low = middle + 1
        else:
            high = middle - 1
    print("{} did not found in the array {}".format(key, arr))


if __name__ == "__main__":
    length = int(input("Please specify the length of the array\n"))
    arr = [randint(10, 100) for i in range(length)]
    print(arr)
    key = int(input("Please inter the key that U wanna to find\n"))
    interpolationSearch(sorted(arr), key)
