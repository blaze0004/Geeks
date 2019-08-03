
from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, src, dest):

        self.graph[src].append(dest)

    def DFS(self):

        visited = [False] * (len(self.graph))

        for i in range(len(self.graph)):

            if not visited[i]:
                self.DFSUtil(i, visited)

    def DFSUtil(self, src, visited):

        visited[src] = True
        print(src, end=' ')

        for i in self.graph[src]:

            if not visited[i]:
                self.DFSUtil(i, visited)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.DFS()