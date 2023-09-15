import heapq

h = [21, 1, 45, 70, 3, 5]

heapq.heapify(h)
print(h)


# https://realpython.com/python-heapq-module/

a = [3, 5, 1, 2, 6, 8, 7]

heapq.heapify(a)

print(a)

heapq.heappop(a)

print(a)

heapq.heappush(a , 4)

print(a)

heapq.heappop(a)

print(a)

heapq.heappop(a)

print(a)

heapq.heappop(a)

print(heapq.nlargest(3, a))

print(heapq.nsmallest(3, a))

