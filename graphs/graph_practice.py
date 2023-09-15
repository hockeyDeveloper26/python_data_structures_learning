from collections import deque

# Exercise - https://www.udemy.com/course/master-the-coding-interview-data-structures-algorithms/learn/lecture/12371828#questions

# Solution - https://www.udemy.com/course/master-the-coding-interview-data-structures-algorithms/learn/lecture/12371830#questions

# -------------------------------------------------------------------------------------------------------------------------------

class Graph:

    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}
    
    def addVertex(self, node):
        self.adjacentList[node] = []
        self.numberOfNodes += 1

    def addEdge(self, node1, node2):
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)

    def showConnections(self):
        allNodes = self.adjacentList.keys()
        for node in allNodes:
            nodeConnections = self.adjacentList[node]
            connections = ""
            for vertex in nodeConnections:
                connections += vertex + " "
            print(f'{node} --> {connections}')



play_graph = Graph()

play_graph.addVertex('0')
play_graph.addVertex('1')
play_graph.addVertex('2')
play_graph.addVertex('3')
play_graph.addVertex('4')
play_graph.addVertex('5')
play_graph.addVertex('6')

play_graph.addEdge('3','1')
play_graph.addEdge('3','4')
play_graph.addEdge('4','2')
play_graph.addEdge('4','5')
play_graph.addEdge('1','2')
play_graph.addEdge('1','0')
play_graph.addEdge('0','2')
play_graph.addEdge('6','5')

play_graph.showConnections()





# https://www.python.org/doc/essays/graphs/

# -----------------------------------------

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph[start]:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: 
                return newpath
    return None


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph[start]:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph[start]:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

def find_shortest_path_BFS(graph, start, end):
    dist = {start: [start]}
    q = deque(start)
    while len(q):
        at = q.popleft()
        for next in graph[at]:
            if next not in dist:
                dist[next] = [dist[at], next]
                q.append(next)
    return dist.get(end)



next_graph = { 'A': ['B', 'C'],
              'B': ['C', 'D'],
              'C': ['D'],
              'D': ['C'],
              'E': ['F'],
              'F': ['C']}

print(find_path(next_graph, 'A', 'D'))
print(find_all_paths(next_graph, 'A', 'D'))
print(find_shortest_path(next_graph, 'A', 'D'))
print(find_shortest_path_BFS(next_graph, 'A', 'D'))