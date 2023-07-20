"""
Depth First Search (DFS) Algorith
Breadth First Search (BFS) Algorith
"""


class Graph:
    def __init__(self, graph=None):
        if graph is None:
            self.graph = {}
        else:
            self.graph = graph

    def addVertex(self, vertex):
        if vertex is not self.graph:
            self.graph[vertex] = []

    def addEdge(self, edge):
        vrt1, vrt2 = tuple(edge)
        if vrt1 in self.graph:
            self.graph[vrt1].append(vrt2)
        else:
            self.graph[vrt1] = []

    def getVertices(self):
        return list(self.graph.keys())

    def getEdges(self):
        return list(self.graph.values())

    def dfs(self, start, visited=None):
        if visited is None:
            visited = []

        visited.append(start)
        remain = set(self.graph[start]) - set(visited)

        for vtx in remain:
            self.dfs(vtx, visited)

        return visited

    def bfs(self, start):
        visited = []
        queue = []
        visited.append(start)
        queue.append(start)

        while queue:
            res = queue.pop(0)
            for val in self.graph[res]:
                if val not in visited:
                    queue.append(val)
                    visited.append(val)
        return visited


data = 'ABCDE'
g = Graph()

for vertex in data:
    g.addVertex(vertex)

edges = [
    ['A', 'B'],
    ['A', 'C'],
    ['A', 'D'],
    ['B', 'A'],
    ['B', 'D'],
    ['B', 'C'],
    ['C', 'A'],
    ['C', 'B'],
    ['C', 'E'],
    ['D', 'B'],
    ['D', 'E'],
    ['D', 'A'],
    ['E', 'C'],
    ['E', 'D'],
]
# edges = [
#     ['A', 'B'],
#     ['A', 'C'],
#     ['B', 'A'],
#     ['B', 'D'],
#     ['C', 'A'],
#     ['C', 'D'],
#     ['D', 'E'],
#     ['E', 'A'],
# ]

for edge in edges:
    g.addEdge(edge)

print(g.getVertices())
print(g.getEdges())
print(g.dfs('A'))
print(g.bfs('A'))
