
from collections import defaultdict
import sys

class MinEdgeReversal:

	def __init__(self, edges, noOfVertices):
		self.V = noOfVertices
		self.graph = defaultdict(list)
		self.addEdge(edges)
	
	def addEdge(self, edges):

		for src, dest in edges:

			self.graph[src].append((dest, 0))
			self.graph[dest].append((src, 1))

	def findMinEdgeReversal(self):

		visited = [False] * (self.V + 1)
		
		disRev = [[0, 0] for i in range(self.V + 1)]

		root = 0
		totalRev = self.DFS(root, visited, disRev)


		result = sys.maxsize
		for i in range(self.V+1):

			edgesToRev = (totalRev - disRev[i][1]) + (disRev[i][0] - disRev[i][1])

			if edgesToRev < result:

				result = edgesToRev
				root = i
		return [root, result]

	def DFS(self, root, visited, disRev):

		visited[root] = True

		totalRev = 0

		for src, isRev in self.graph[root]:

			if not visited[src]:

				visited[src] = True

				disRev[src][0] = disRev[root][0] + 1
				disRev[src][1] = disRev[root][1]

				if isRev:
					disRev[src][1] = disRev[root][1] + 1
					totalRev += 1

				totalRev += self.DFS(src, visited, disRev)

		return totalRev


edges = [
	(0, 1),
	(2, 1),
	(3, 2),
	(3, 4),
	(5, 4),
	(5, 6),
	(7, 6)
]

graph = MinEdgeReversal(edges, len(edges))
root, edges = graph.findMinEdgeReversal()
print({'root': root, 'minEdge': edges})