#!/usr/bin/python3

from random import randint

# Thsi is the complete counting sort implementation
def countingSort(arr):
    Augarr = [0] * (max(arr) + 1)

    for item in arr:
        Augarr[item] += 1

    sortedArr = []
    for i in range(len(Augarr)):
        while Augarr[i] != 0:
            sortedArr.append(i)
            Augarr[i] -= 1

    arr = sortedArr
    return arr

if __name__=="__main__":
    n = int(input("Enter array length:\n"))
    arr = [randint(0, 100) for i in range(n)]
    print(arr)
    print(countingSort(arr))
