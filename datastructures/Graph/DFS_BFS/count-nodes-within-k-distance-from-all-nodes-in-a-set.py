
from Graph import UnDirectedGraph
import sys

class KDistance(UnDirectedGraph):

	def __init__(self):
		UnDirectedGraph.__init__(self)

	def BFS(self, src, marked, findMinMax = False):

		queue = [src]
		currV = [0] * (self.V)

		currV[src] = 1

		while queue:

			v = queue.pop(0)

			for i in self.graph[v]:

				if self.visited[i] > k+1:
					currV[i] = self.visited[i]
					self.visited[i] = 0
					queue.append(i)
					continue

				if not currV[i]:

					currV[i] = currV[v] + 1
					queue.append(i)
		# print(currV)
		self.visited = currV
		#print(list(map(lambda x: x-1, self.visited)))
		if findMinMax:
			a = -1
			v = 0
			for m in marked:

				if a < currV[m] - 1:
					a = currV[m] - 1
					v = m

			a = sys.maxsize
			u = 0 
			for m in marked:

				if a > currV[m] - 1:
					a = currV[m] - 1
					u = m

			return [u, v]

		del currV
		return self.visited



	def countNodesAtKDistFromMarked(self, marked, k):

		self.visited = [0] * (self.V)

		# First BFS to find max distances
		u, v = self.BFS(0, marked, True)

		# if u == 0:
		# 	self.BFS(v, marked)
		# elif v == 0:
		# 	self.BFS(u, marked)
		# else:
		self.visited = [0] * (self.V)
		visited1 = self.BFS(u, marked)
		self.visited = [0] * (self.V)
		visited2 = self.BFS(v, marked)

		nodeCount = 0
		#print(self.visited)
		for i in range(self.V):
			if visited1[i]-1 <= k and visited2[i]-1 <= k:
				nodeCount += 1

		del self.visited
		del visited1, visited2, u, v
		return nodeCount

graph = KDistance()

graph.addEdge(1, 0)
graph.addEdge(0, 3)
graph.addEdge(0, 8)
graph.addEdge(10, 11)
graph.addEdge(11, 3)
graph.addEdge(11, 5)
graph.addEdge(2, 3)
# graph.addEdge(3, 5)
graph.addEdge(3, 6)
graph.addEdge(3, 7)
graph.addEdge(4, 5)
graph.addEdge(5, 9)

marked = [1, 2, 4, 10]
k = 3
nodeCount = graph.countNodesAtKDistFromMarked(marked, k)
print(nodeCount)
# [1, 0, 3, 2, 4, 3, 3, 3, 2, 4]
# [3, 4, 3, 2, 4, 1, 2, 2, 4, 4]
# [2, 3, 0, 1, 4, 2, 2, 2, 3, 4] [3, 3, 3, 3, 8, 5, 5, 5, 5, 8]
# [3, 4, 3, 2, 4, 1, 3, 3, 4, 4] [6, 7, 6, 5, 12, 6, 8, 8, 9, 12] [3, 4, 3, 2, 9, 3, 5, 5, 6, 9]
