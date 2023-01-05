# usr/bin/python3

from random import randint

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i = j =k =0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:

                arr[k] = lefthalf[i]
                i += 1
            else:
                arr[k] = righthalf[j]
                j+=1
            k+=1
        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i+=1
            k+=1
        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1

    return arr


if __name__ == "__main__":
    array = [randint(10, 100) for i in range(10)]
    original = array
    print("Original array: {}".format(original))
    sorted_array = mergeSort(array)
    print("Sorted array: {}".format(sorted_array))
