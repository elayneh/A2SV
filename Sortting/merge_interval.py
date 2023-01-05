# Given array of intervals where interevals[i] = [start, end]. merge all overlapping intervals
# and return an array of non overlapping  intervals that cover all the intervals in the input.

def interval_merger(arr):
    index = 0
    for i in range(len(arr) -1):
        if arr[i][len(arr[i]) - 1] > arr[i + 1][0]:
            arr[index][1] = max(arr[index][1], arr[i][1])
        else:
            index+=1
            arr[index] = arr[i]

    print("The merged interevala are: ",end=" ")
    for i in range(index + 1):
        print(arr[i], end=" ")

if __name__ == "__main__":
    arr = [[1,3], [2, 6], [10, 20], [8, 38]]
    interval_merger(arr)
