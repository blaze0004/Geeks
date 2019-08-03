
from collections import defaultdict

class Graph:

    def __init__(self, vertices):

        self.V = vertices
        self.graph = defaultdict(list)
        self.tc = [[0 for i in range(vertices)] for j in range(vertices)]
        print(self.tc)

    def addEdge(self, src, dest):
        self.graph[src].append(dest)

    def DFSUtil(self, src, dest):

        self.tc[src][dest] = 1

        for i in self.graph[src]:

            if self.tc[src][i] == 0:
                self.DFSUtil(src, i)

    def transitiveClosure(self):

        for i in range(self.V):
            self.DFSUtil(i, i)

        for i in self.tc:
            print(i)
g = Graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print("Transitive closure matrix is")
g.transitiveClosure(); 
