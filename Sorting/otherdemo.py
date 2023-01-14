def insertion(arr):
    for i in range(len(arr)):
        j = i
        while arr[j] < arr[j - 1] and j > 0:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

        if i > 0:
            print(*arr)



if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    insertion(arr)
