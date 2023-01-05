# usr/bin/python3
from random import randint

"""Is not a comparision sort and
it assumes that each of the elements are an integer in the range of 1 to k for some integer k
"""

def countingSort(arr, k):
    B = [0 for elet in arr]
    C = [0 for elet in range(k +1)]
    for i in range(k+1):
        C[i] = 0
    for j in range(len(arr)):
        C[arr[j]] += 1
    for i in range(1, k+1):
        C[i] += C[i - 1]
    for j in range(len(arr) - 1, -1, -1):
        temp = arr[j]
        temp2 = C[temp] - 1
        B[temp2] = temp
        C[temp] -= 1

    return B

if __name__=="__main__":
    arr = [randint(10, 100) for i in range(10)]
    Original_array = arr
    Sorted_array = countingSort(arr, 1000)
    print("Original array: {}".format(Original_array))
    print("Sorted array {}".format(Sorted_array))
