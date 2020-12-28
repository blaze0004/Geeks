
import sys
from Graph import UnDirectedGraph
class Graph(UnDirectedGraph):

	def __init__(self, N):
		UnDirectedGraph.__init__(self)
		self.V = N

	def addEdge(self, x1, x2, y1, y2):

		a = (x1 - 1) * self.V + y1
		b = (x2 - 1) * self.V + y2

		self.graph[a].append(b)
		self.graph[b].append(a)
	
	def countNotAccessible(self):

		visited = [0] * (self.V*self.V)

		result = 0

		for i in range(1, self.V * self.V + 1):

			if not visited[i]:

				self.

n = int(input('Enter block size\n'))
noOfAccessiblePath = int(input('Enter number of accessiblePath')) 
graph = Graph(n)
for i in range(noOfAccessiblePath):

	x1, y1, x2, y2 = map(int, input().split())
	graph.addAccessiblePath(x1, x2, y1, y2)
print(graph.graph)