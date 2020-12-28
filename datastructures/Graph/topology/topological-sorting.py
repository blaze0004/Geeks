
from Graph import DirectedGraph

class TopologicalSorting(DirectedGraph):
    """docstring for TopologicalSorting"""
    def __init__(self):
        DirectedGraph.__init__(self)

        self.V = 0

    def addEdge(self, src, dest):

        self.V += 1

        self.graph[src].append(dest)

    def doTopologicalSortUtil(self, src, visited, stack):
        visited[src] = True
        for dest in self.graph[src]:
            if not visited[dest]:
                self.doTopologicalSortUtil(dest, visited, stack)
        stack.insert(0, src)
    def doTopologicalSort(self):
        # print(self.V)
        visited = [False] * (self.V)
        stack = []
        for i in range(self.V):
            if not visited[i]:
                self.doTopologicalSortUtil(i, visited, stack)
            # print(i)

        print(stack)
g= TopologicalSorting() 
g.addEdge(5, 2); 
g.addEdge(5, 0); 
g.addEdge(4, 0); 
g.addEdge(4, 1); 
g.addEdge(2, 3); 
g.addEdge(3, 1);


g.doTopologicalSort()
