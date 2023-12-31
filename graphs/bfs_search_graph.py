import collections

def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end ="")

        # If not visited, mark it as visited, and enqueue it
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
print('This is Breadth First Traversal of Graph')
print(bfs(graph, 0))