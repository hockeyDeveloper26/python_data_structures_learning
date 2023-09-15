
# deque is Linked Lists in Python

from collections import deque

# Create Linked List

# ========================================================

linked_list = deque() # empty

ll = deque('abc')   # Strings are iterable like Arrays

print(ll)

ll2 = deque(['a','b','c','d'])

print(ll2)

ll3 = deque([{'data': 'a'}, {'data': 'b'}])

print(ll3)


ll2.append('e') # Add to Linked List (Deque)

print(ll2)

ll2.pop() # Remove from right side of Linked List. If no index given, removes last item

print(ll2)

ll2.appendleft('e') # Append Left Side

print(ll2)

ll2.popleft() # Pop Left Side

print(ll2)


# Queues are set up the same way. For FIFO, use append to add at end and popleft to remove first in.

queue = deque()

