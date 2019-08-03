from collections import defaultdict


class Graph:

    def __init__(self):

        self.graph = defaultdict(list)
        print(self.graph)

    def addEdge(self, src, dest):
        self.graph[src].append(dest)

    def BFS(self, src):

        visited = [False] * (len(self.graph))

        queue = [src]

        visited[src] = True

        while queue:

            src = queue.pop(0)

            print(src, end=' ')

            for i in self.graph[src]:

                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        # print(self.graph)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print('Following is BFS with source vertex 2')
g.BFS(2)
