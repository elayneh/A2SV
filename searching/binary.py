#usr/bin/python3
from random import randint

"""Time complexity of the algorithm is O(logn).
Space complexity O(1)
"""

def binarySearch(arr, key):
    low = 0
    high = len(arr) - 1
    while(low <= high):
        middle = (low + high) // 2
        if arr[middle] == key:
            print("{} is found at the position {}".format(key, middle))
            return
        elif arr[middle] < key:
            low = middle + 1
        else:
            high = middle - 1
    print("{} did not found in the array: {}".format(key, arr))
    return

if __name__ == "__main__":
    length = int(input("Please specify the length of the array:\n"))
    arr = [randint(10, 100) for i in range(length)]
    print(arr)
    key  = int(input("Please Enter the key U wanna to search\n"))

    binarySearch(arr, key)
