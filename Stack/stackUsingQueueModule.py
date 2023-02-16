from queue import LifoQueue

stack = LifoQueue(maxsize = 3)

print(stack.qsize())
print(stack.maxsize)
print(stack.empty())
stack.put('a')
print(stack.get_nowait()) # Return empty if no item is available
stack.put('A')
stack.put('b')
stack.put('B') # wait until free space is found
print(stack.get()) # if no item found wait until item is available
stack.put('this is the final item to be put')
print(stack.full())
stack.put_nowait(23)
