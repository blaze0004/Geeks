
from Graph import UnDirectedGraph

class DetectCycleInUndirectedGraph(UnDirectedGraph):
	"""docstring for DetectCycleInUndirectedGraph"""
	def __init__(self):
		super(DetectCycleInUndirectedGraph, self).__init__()
		
	def isCycle(self, start):

		visited = [False] * (self.V + 1)

		for i in range(self.V):

			if not visited[i]:

				if self.DFS(i, visited, -1):
					return True

		return False

	def DFS(self, src, visited, parent):

		visited[src] = True

		for i in self.graph[src]:

			if not visited[i]:

				if self.DFS(i, visited, src):
					return True

				elif parent != i:
					return True

		return False

edges = [(1, 2), (1, 0), (0, 3), (3, 4)]

graph = DetectCycleInUndirectedGraph()

for src, dest in edges:

	graph.addEdge(src, dest)

print(graph.graph)

print(graph.isCycle(0))