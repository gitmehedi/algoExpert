"""
Basic Operations in Graph Algorith
==================================
- Display graph vertices
- Display graph edges
- Add a vertex
- Add an edge
- Creating a graph
"""


class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    # Get the keys of the dictionary
    def getVertices(self):
        return list(self.gdict.keys())

    def getEdges(self):
        return list(self.gdict.values())

    def addVertex(self, vertex):
        if vertex not in self.gdict:
            self.gdict[vertex] = []

    def addEdge(self, edge):
        vt1, vt2 = tuple(edge)
        if vt1 in self.gdict:
            self.gdict[vt1].append(vt2)
        else:
            self.gdict[vt1] = [vt2]


# Create the dictionary with graph elements
graph_vertices = 'ABCDE'
g = graph()
for vertex in graph_vertices:
    g.addVertex(vertex)

g.addEdge({'A', 'B'})
g.addEdge({'A', 'C'})
g.addEdge({'C', 'B'})

print(g.getVertices())
print(g.getEdges())
