#usr/bin/python3

from random import randint

"""Time complexity of this algorithm is O(n).
Space complexity of the algorithm is O(1).
"""

def orderedLinearSearch(arr, key):
    for i in range(len(arr)):
        if arr[i] > key:
            print("{} did not found in the array: {}".format(key, arr))
            return
        if arr[i] == key:
            print("{} is found at position {}th of array: {}".format(key, i, arr))
            return

    return


if __name__=="__main__":
    length = int(input("Please specify the length of the array:\n"))
    arr = [randint(10, 100) for i in range(length)]
    print(arr)
    key  = int(input("Please Enter the key U wanna to search\n"))

    orderedLinearSearch(sorted(arr), key)

