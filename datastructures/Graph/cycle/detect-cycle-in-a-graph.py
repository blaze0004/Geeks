
from Graph import DirectedGraph

class DetectCycle(DirectedGraph):

	def __init__(self):

		DirectedGraph.__init__(self)

	def clearGraph(self):

		DirectedGraph.__init__(self)

	def isCycle(self, start):

		visited = [False] * (self.V+1)
		recStack = [False] * (self.V+1)

		print('Contain Cycle') if self.DFS(start, visited, recStack) else print('No Cycle')


	def DFS(self, src, visited, recStack):

		visited[src] = True
		recStack[src] = True

		for neighbour in self.graph[src]:

			if not visited[neighbour]:

				visited[neighbour] = True

				if self.DFS(neighbour, visited, recStack):
					return True
				else:
					return False
			elif recStack[neighbour]:
				return True

		recStack[src] = False
		return False

graph = DetectCycle()

edges1 = [(2, 0), (0, 2), (0, 1), (1, 2), (2, 3), (3,3)]
edges2 = [(1, 2), (2, 0), (0, 1), (2, 3), (3, 3)]
edges3 = [(0, 1), (0, 2), (1, 3), (1, 4), (3, 6), (4, 6), (2, 5), (5, 4), (5, 6)]

for src, dest in edges1:

	graph.addEdge(src, dest)

print(graph.isCycle(2))
graph.clearGraph()
for src, dest in edges2:

	graph.addEdge(src, dest)

print(graph.isCycle(1))
graph.clearGraph()
for src, dest in edges3:

	graph.addEdge(src, dest)

print(graph.isCycle(0))

