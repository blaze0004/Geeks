
from collections import defaultdict

class Graph:

	def __init__(self, vertices):
		self.V = vertices
		self.graph = defaultdict(list)

	def addEdge(self, src, dest):

		self.graph[src].append(dest)

	def addEdgeFromArray(self, arr):

		for i in range(1, self.V):

			self.addEdge(arr[i], i)


	def findHeight(self):

		visited = [0] * (self.V)

		visited[0] = 1

		queue = [0]

		while queue:

			s = queue.pop(0)

			for i in self.graph[s]:
				if not visited[i]:
					visited[i] = visited[s] + 1
					queue.append(i)


		return max(visited) - 1

	def findHeightInOneIter(self, arr):

		height = [0] * self.V

		for i in range(1,self.V):

			height[i] = height[arr[i]] + 1

		return max(height)

arr = [-1, 0, 1, 2, 3]

graph = Graph(len(arr))

graph.addEdgeFromArray(arr)
height = graph.findHeight()
heightInOne = graph.findHeightInOneIter(arr)
print(height)
print(heightInOne)