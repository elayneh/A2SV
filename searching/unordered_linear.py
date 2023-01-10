#usr/bin/python3

from random import randint

"""
Time complexity O(n), in the worst case we need to scan entire array element, and
The space complexity is O(1).
"""
def unorderedLinearSearch(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            print("{} is found at {}th position.".format(key, i))
            return
    print("{} is not found in the array {}".format(key, arr))
    return



if __name__=="__main__":
    length = int(input("Please specify the length of the array:\n"))
    arr = [randint(10, 100) for i in range(length)]
    print(arr)
    key  = int(input("Please Enter the key U wanna to search\n"))

    unorderedLinearSearch(arr, key)
