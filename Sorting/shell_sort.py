# usr/bin/python3
from random import randint

"""Also known as diminishing increment sort
Generalization of insertion sort
The variation used in shell sort is to avoid comparing
adjecent elements until the last step of the algorithm.
So the last step of shell sort is effectively insertion sort algorithm
Increase the efficiency of insertion sort by quickly shifting values to their destination

Efficient for medium size lists. and it is the fastest of all O(n2) sorting algorithms
"""


def shellSort(arr):
    sublistcount = len(arr) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(arr, startposition, sublistcount)
        print("After increment of size {} The list is {}".format(sublistcount, arr))
        sublistcount = sublistcount // 2
def gapInsertionSort(arr, start, gap):
    for i in range(start + gap, len(arr), gap):
        currentvalue = arr[i]
        position = i
        while position >= gap and arr[position - gap] > currentvalue:
            arr[position] = arr[position - gap]
            position = position - gap
        arr[position] = currentvalue


if __name__ == "__main__":
    arr = [randint(10, 100) for i in range(10)]
    print("Original array: ",arr)
    sorted_array = shellSort(arr)
    print(sorted_array)
