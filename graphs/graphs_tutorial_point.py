# https://www.tutorialspoint.com/python_data_structure/python_graphs.htm

# Create dictionary with graph elements

class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict
    
    # Get the keys of the dictionary
    def getVertices(self):
        return list(self.gdict.keys())
    
    # Add the vertex as key
    def addVertex(self, vrtx):
        if vrtx not in self.gdict:
            self.gdict[vrtx] = []
    

    # Display Graph Edges
    def edges(self):
        return self.findedges()
    
    # Add New Edge
    def AddEdge(self, edge):
        edge = set(edge)
        {vrtx1, vrtx2} = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]
    
    # Find the distinct list of edges
    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename
    


    
# Create the dictionary with graph elements
graph_elements = {
    "a" : ["b", "c"],
    "b" : ["a", "d"],
    "c" : ["a", "d"],
    "d" : ["e"],
    "e" : ["d"]
}

g = graph(graph_elements)
print(g.getVertices())
print(g.edges())

g.addVertex("f")
print(g.getVertices())

g.AddEdge({'a','e'})
g.AddEdge({'a','c'})
print(g.edges())



# graph_dictionary = {
#     "a" : ["b", "c"],
#     "b" : ["a", "d"],
#     "c" : ["a", "d"],
#     "d" : ["e"],
#     "e" : ["d"]
# }

# print(graph_dictionary)