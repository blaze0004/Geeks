
from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def DFSUtil(self, src, visited):

        visited[src] = True

        for i in self.graph[src]:

            if not visited[i]:
                self.DFSUtil(i, visited)


    def addEdge(self, src, dest):
        self.graph[src].append(dest)

    def findMother(self):

        visited = [False] * (self.V)

        v = 0

        for i in range(self.V):

            if not visited[i]:
                self.DFSUtil(i, visited)
                v = i

        visited = [False] * (self.V)

        self.DFSUtil(v, visited)
        if any(not i for i in visited):
            return -1
        return v
    
g = Graph(7) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 3) 
g.addEdge(4, 1) 
g.addEdge(6, 4) 
g.addEdge(5, 6) 
g.addEdge(5, 2) 
g.addEdge(6, 0)

print('A mother vertex is {}'.format(g.findMother()))


        
        
