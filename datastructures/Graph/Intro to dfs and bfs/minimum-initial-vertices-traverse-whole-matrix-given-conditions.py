# Condition: move to only neighbour having value <= current cell
# neighbour: all sides

import sys

class Graph:

        def __init__(self, vertices):
                self.V = vertices
                self.graph = [[0 for i in range(self.V)] for j in range(self.V)]
                self.maxV = []
                self.visited = [[False for i in range(self.V)] for j in range(self.V)]

        def addEdge(self, src, dest, value):
                self.graph[src][dest] = value

               # print(self.graph[src][dest])
                self.maxV.append((src, dest, value))

        def findMinimum(self):

                self.maxV.sort(key=lambda x: x[2], reverse=True)


                for v in self.maxV:

                        src, dest = v[0], v[1]

                        if not self.visited[src][dest]:

                                self.visited[src][dest] = True
                                print(src, dest)
                                self.DFS(src, dest)

        def DFS(self, src, dest):
                if  src + 1 < self.V and not self.visited[src+1][dest] and self.graph[src][dest] >= self.graph[src+1][dest]:
                        self.visited[src+1][dest] = True
                        self.DFS(src+1, dest)

                if dest - 1 >= 0 and not self.visited[src][dest-1] and self.graph[src][dest] >= self.graph[src][dest-1]:
                        self.visited[src][dest-1] = True
                        self.DFS(src, dest-1)

                if src - 1 >= 0 and not self.visited[src-1][dest] and self.graph[src][dest] >= self.graph[src-1][dest]:
                        self.visited[src-1][dest] = True
                        self.DFS(src-1, dest)

                if dest + 1 < self.V and not self.visited[src][dest+1] and self.graph[src][dest] >= self.graph[src][dest+1]:
                        self.visited[src][dest+1] = True
                        self.DFS(src, dest+1)

        def printGraph(self):
                for i in self.graph:
                        print(i)
graph = Graph(int(input()))

for src in range(graph.V):
        data = [int(x) for x in input().split()]
        for dest in range(len(data)):
                val = data[dest]
                graph.addEdge(src, dest, val)

graph.findMinimum()
