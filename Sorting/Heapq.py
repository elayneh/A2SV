#!/usr/bin/python3

"""
Heap queue is a special tree structure in which each parent node is less than or equal to its child node.
It is implemented using the heapq module.
It is very useful is implementing priority queues where the queue item with higher weight is given more priority in processing.

heapq module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm.
Heaps are binary trees for which every parent node has a value less than or equal to any of its children.



heapq functions:
    heapify(iterable) -> To convert iterable into a heap DS
    heappush(heap, element) -> insert the element into heap
    heappop(heap) -> remove and return the smallest element from the heap
    heappushpop(heap, element) -> both push and pop operation in one statement, increasing efficiency
    heapreplace(heap, element) -> inserts and pops element in one statement, but different from the above statement.
    nlargest(k, iterable, k=fun) -> Return k largest elements from the iterable specified and satisfy the key if mentioned
    nsmallest(k, iterable, key=fun) -> Return k smallest elements from the iterable specified and satisfy the key if mentioned

"""
import heapq as heap


List= [1,10,2,8,3,0]
print("The original list: {}".format(List))

heap.heapify(List)
print("The created heap is: {}".format((List)) )
heap.heappush(List, 100)
print("The modified heap after push is: {}".format((List)))
heap.heappop(List)
print("The modified heap after pop is: {}".format(List))
print("The popped element using heappushpop() is: ", heap.heappushpop(List, 777))
print("The modified heap after heappushpop() is: ", List)
print("The pushed element using heapreplace() is: ", heap.heapreplace(List, 777))
print("The modified heap after heapreplace()) is: ", List)
print("The 3 largest numbers in list are: ", heap.nlargest(3, List))
print("The 3 smallest numbers from the list is: ", heap.nsmallest(3, List))

