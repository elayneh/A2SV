from random import randint
def isArraySorted(arr):
    if len(arr) == 1:
        return True
    return arr[0] <= arr[1] and isArraySorted(arr[2:])


if __name__ == "__main__":
    n = int(input("Enter array length\n"))
    arr = [randint(1, 10) for i in range(n)]
    print(isArraySorted(arr))
