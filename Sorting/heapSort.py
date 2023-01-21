def heapify(l, n, start):
    largest = start
    left = 2 * start + 1
    right = 2 * start + 2

    if left < n and l[left] > l[largest]:
        largest = left
    if right < n and l[right] > l[largest]:
        largest = right

    if largest != start:
        l[start], l[largest] = l[largest], l[start]
        heapify(l, n, largest)


def buildHeap(l, n,):
    startPoint = n // 2 -1
    for idx in range(startPoint, -1, -1):
        heapify(l, n, idx)

def heapSort(l, n):
    buildHeap(l, n)
    for i in range(n - 1, 0, -1):
        l[0], l[i] = l[i], l[0]
        heapify(l, i, 0)
    print("List after sort operation will be: {}".format(l))

def printter(l, n):
    print("List representation of Heap is:")
    print(l)

if __name__ == "__main__":
    List = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
    
    n = len(List)
    buildHeap(List, n)
    printter(List, n)
    heapSort(List, n)
